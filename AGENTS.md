# Copilot Agent Guidelines

This file contains standing instructions for the Copilot coding agent working on this repository.

## Before Every Commit

Always verify all of the following pass before creating a commit or reporting progress:

1. **Tests** – `uv run pytest -q` must have 0 failures.
2. **Lint** – `uv run --group lint ruff check src/mypackage/` must report no issues.
3. **Format** – `uv run --group lint ruff format --check src/mypackage/` must report no files to reformat.
4. **Type checks** – run `uv run --group typecheck ty check src/mypackage` (or `make typecheck`) and fix any type errors in changed files.

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
