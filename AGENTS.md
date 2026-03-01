# Agent Guidelines

This file contains standing instructions for **all** coding agents working on this repository (Copilot, Claude, etc.).

## Before Every Commit

**All agents must** verify that every one of the following passes before creating a commit or reporting progress. No exceptions.

1. **Tests** – `uv run pytest -q` (or `make test`) must have 0 failures.
2. **Lint** – `uv run --group lint ruff check src/mypackage/` (or `make lint`) must report no issues.
3. **Format** – `uv run --group lint ruff format --check src/mypackage/` must report no files to reformat.
4. **Type checks** – `uv run --group typecheck ty check src/mypackage` (or `make typecheck`) must report no errors in changed files.

## Commit Messages

All commit messages **must** follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

Examples:
- `feat: add new data loading utility`
- `fix: correct off-by-one error in slice computation`
- `docs: update installation instructions`
- `chore: bump ruff to 0.9.7`
