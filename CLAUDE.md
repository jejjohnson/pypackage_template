# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

<!-- TODO: Replace with your project description -->
A Python package. Built with Python 3.12+, uv, pytest, and MkDocs.

## Common Commands

```bash
make install              # Install all deps (uv sync --all-groups) + pre-commit hooks
make test                 # Run tests: uv run pytest -v
make format               # Auto-fix: ruff format . && ruff check --fix .
make lint                 # Lint code: ruff check .
make typecheck            # Type check: ty check src/mypackage
make precommit            # Run pre-commit on all files
make docs-serve           # Local docs server
```

### Running a single test

```bash
uv run pytest tests/test_example.py::TestClass::test_method -v
```

### Pre-commit checklist (all four must pass)

```bash
uv run pytest -v                              # Tests + doctests
uv run --group lint ruff check .              # Lint — ENTIRE repo, not just src/mypackage/
uv run --group lint ruff format --check .     # Format — ENTIRE repo
uv run --group typecheck ty check src/mypackage  # Typecheck — package only
```

**Critical**: Always lint/format with `.` (repo root), not `src/mypackage/`. CI runs `ruff check .` which includes `tests/`, `scripts/`, **and the code cells of `docs/notebooks/*.ipynb`**.

`--doctest-modules` is in `addopts` and `src/mypackage` is a `testpath`, so every `Examples:` block in a docstring is executed on each run. When you change behaviour, update the examples — and verify the expected output against what the code actually prints.

### Building the docs

```bash
uv run --group docs mkdocs build --strict   # what CI runs; broken refs fail
```

## Architecture

### Package structure

All implementation lives in `src/mypackage/`. The public API is re-exported through `src/mypackage/__init__.py`, and `__all__` there is the contract — `tests/test_public_api.py` enforces it.

| Module | Contents |
|---|---|
| `_typing.py` | PEP 695 `type` aliases + runtime-checkable `Transform` / `Fittable` protocols |
| `exceptions.py` | `MypackageError` hierarchy; each member also subclasses the nearest stdlib exception |
| `utils.py` | Validators (`as_floats`, `require_non_empty`, `require_positive`), generic `Window[T]`, `timer()` |
| `stats.py` | `summarize`/`Summary`, `quantile`, `zscores`, `RunningStats` (Welford) |
| `smoothing.py` | `moving_average`, `exponential_moving_average`, `median_filter`, `Padding` |
| `transforms.py` | `Standardize`, `MinMaxScale`, `Clip`, `MovingAverage`, `Pipeline`, `chain` |
| `cli.py` | `argparse` console script (`mypackage summarize|smooth`), wired via `[project.scripts]` |

Dependency direction is strictly one-way:
`_typing` → `exceptions` → `utils` → `stats` → `smoothing` → `transforms` → `cli`.

### Invariants the tests enforce

- Every public function returns a **new** list and never mutates its input.
- Inputs are validated once, at the public boundary, via the `utils` validators.
- Stateful transforms raise `NotFittedError` before `fit`, never a silent identity.
- `Transform` is structural, so user-defined transforms compose without a base class.

### Key directories

| Path | Purpose |
|------|---------|
| `src/mypackage/` | Main package source code |
| `tests/` | Test suite |
| `docs/guide/` | Hand-written guide pages |
| `docs/api/` | mkdocstrings API reference, one page per module |
| `docs/notebooks/` | Executed example notebooks (outputs committed) |
| `notebooks/` | Scratch Jupyter notebooks |
| `scripts/` | Example scripts |

## Documentation Examples

Example notebooks live in `docs/notebooks/` as jupytext percent-format `.py` files. The workflow:

1. Write the `.py` source (jupytext percent format)
2. Convert and execute: `jupytext --to notebook foo.py` then `jupyter nbconvert --execute --inplace foo.ipynb`
3. Delete the `.py` — the executed `.ipynb` is the committed source of truth
4. `mkdocs-jupyter` renders the pre-executed `.ipynb` with `execute: false`

Figures render inline via `plt.show()` — do **not** use `savefig` or commit separate PNG files. The `.ipynb` cell outputs are the single source of rendered figures.

See `.github/instructions/docs-examples.instructions.md` for full standards.

## Coding Conventions

- Google-style docstrings
- `dataclasses` or `attrs` for data containers
- Type hints on all public functions and methods
- Pure functions where possible; side effects isolated and explicit
- Surgical changes only — don't refactor adjacent code or add docstrings to unchanged code

## Plans

Plans and design documents go in `.plans/` (gitignored, never committed). Track work via GitHub issues instead.

## PR Review Comments

When addressing PR review comments, always resolve each review thread after fixing it via the GitHub GraphQL API (`resolveReviewThread` mutation). Do not leave addressed comments unresolved. To obtain the required `threadId`, first list the pull request's review threads via the GitHub GraphQL API (see the "Pull Request Review Comments" section in `AGENTS.md` for a minimal query and end-to-end workflow).

## Code Review

Follow the guidance in `/CODE_REVIEW.md` for all code review tasks.
