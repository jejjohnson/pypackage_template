"""Tests for ``mypackage.cli``.

`main` takes explicit streams, so the whole CLI is testable without
monkeypatching `sys.stdout` or spawning a subprocess.
"""

from __future__ import annotations

import io
import json
from pathlib import Path

import pytest

import mypackage
from mypackage.cli import EXIT_ERROR, EXIT_OK, build_parser, main


def run(*argv: str, stdin: str | None = None) -> tuple[int, str, str]:
    """Run the CLI and capture ``(status, stdout, stderr)``."""
    out, err = io.StringIO(), io.StringIO()
    status = main(
        list(argv),
        out=out,
        err=err,
        stdin=io.StringIO(stdin) if stdin is not None else None,
    )
    return status, out.getvalue(), err.getvalue()


class TestParser:
    def test_defaults_to_stdin(self) -> None:
        args = build_parser().parse_args(["summarize"])
        assert args.path == "-"

    def test_subcommand_is_required(self) -> None:
        with pytest.raises(SystemExit):
            build_parser().parse_args([])

    def test_smooth_defaults(self) -> None:
        args = build_parser().parse_args(["smooth"])
        assert (args.method, args.window, args.alpha, args.padding) == (
            "mean",
            3,
            0.3,
            "edge",
        )

    def test_rejects_an_unknown_method(self) -> None:
        with pytest.raises(SystemExit):
            build_parser().parse_args(["smooth", "--method", "kalman"])


class TestSummarize:
    def test_table_output(self) -> None:
        status, out, err = run("summarize", "-", stdin="1 2 3 4")
        assert status == EXIT_OK
        assert err == ""
        assert "mean" in out
        assert "2.5" in out

    def test_json_output(self) -> None:
        status, out, _ = run("summarize", "-", "--json", stdin="1 2 3 4")
        payload = json.loads(out)
        assert status == EXIT_OK
        assert payload["count"] == 4
        assert payload["mean"] == pytest.approx(2.5)
        assert payload["median"] == pytest.approx(2.5)

    def test_reads_from_a_file(self, series_file: Path) -> None:
        status, out, _ = run("summarize", str(series_file), "--json")
        assert status == EXIT_OK
        assert json.loads(out)["count"] == 5

    def test_comma_separated_input(self) -> None:
        _, out, _ = run("summarize", "-", "--json", stdin="1,2,3,4")
        assert json.loads(out)["count"] == 4

    def test_newline_separated_input(self) -> None:
        _, out, _ = run("summarize", "-", "--json", stdin="1\n2\n3\n")
        assert json.loads(out)["count"] == 3

    def test_ddof_is_forwarded(self) -> None:
        _, out, _ = run("summarize", "-", "--json", "--ddof", "0", stdin="1 2 3 4 5")
        assert json.loads(out)["variance"] == pytest.approx(2.0)


class TestSmooth:
    def test_mean_is_the_default_method(self) -> None:
        status, out, _ = run("smooth", "-", "--precision", "3", stdin="1 2 3 4 5")
        assert status == EXIT_OK
        assert out.split() == ["1.333", "2.000", "3.000", "4.000", "4.667"]

    def test_median_removes_a_spike(self) -> None:
        _, out, _ = run(
            "smooth",
            "-",
            "--method",
            "median",
            "--precision",
            "1",
            stdin="1 1 99 1 1",
        )
        assert out.split() == ["1.0"] * 5

    def test_ewma(self) -> None:
        _, out, _ = run(
            "smooth",
            "-",
            "--method",
            "ewma",
            "--alpha",
            "0.5",
            "--precision",
            "2",
            stdin="1 2 3",
        )
        assert out.split() == ["1.00", "1.50", "2.25"]

    def test_padding_is_forwarded(self) -> None:
        _, out, _ = run(
            "smooth",
            "-",
            "--padding",
            "none",
            "--precision",
            "1",
            stdin="1 2 3 4 5",
        )
        assert out.split() == ["2.0", "3.0", "4.0"]

    def test_window_is_forwarded(self) -> None:
        _, out, _ = run(
            "smooth", "-", "--window", "5", "--precision", "1", stdin="1 2 3 4 5"
        )
        assert len(out.split()) == 5


class TestErrorHandling:
    def test_empty_input_is_reported(self) -> None:
        status, out, err = run("summarize", "-", stdin="")
        assert status == EXIT_ERROR
        assert out == ""
        assert err.startswith("error: ")
        assert "at least one value" in err

    def test_non_numeric_input_is_reported(self) -> None:
        status, _, err = run("summarize", "-", stdin="1 2 banana")
        assert status == EXIT_ERROR
        assert "only numbers" in err

    def test_missing_file_is_reported(self, tmp_path: Path) -> None:
        status, _, err = run("summarize", str(tmp_path / "nope.txt"))
        assert status == EXIT_ERROR
        assert "could not read" in err

    def test_window_larger_than_series_is_reported(self) -> None:
        status, _, err = run("smooth", "-", "--window", "99", stdin="1 2 3")
        assert status == EXIT_ERROR
        assert "must not exceed the series length" in err


class TestMeta:
    def test_version_flag_exits_cleanly(self) -> None:
        assert main(["--version"], out=io.StringIO(), err=io.StringIO()) == EXIT_OK

    def test_help_exits_cleanly(self) -> None:
        assert main(["--help"], out=io.StringIO(), err=io.StringIO()) == EXIT_OK

    def test_usage_error_returns_two(self) -> None:
        assert main(["nonsense"], out=io.StringIO(), err=io.StringIO()) == 2

    def test_entry_point_is_declared(self) -> None:
        """`mypackage = "mypackage.cli:main"` must stay wired in pyproject."""
        pyproject = Path(mypackage.__path__[0]).parents[1] / "pyproject.toml"
        if not pyproject.is_file():  # installed without the source tree
            pytest.skip("source checkout not available")
        assert 'mypackage = "mypackage.cli:main"' in pyproject.read_text(
            encoding="utf-8"
        )
