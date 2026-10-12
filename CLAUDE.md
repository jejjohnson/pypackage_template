# CLAUDE.md

The rules for every agent live in `AGENTS.md`; this file adds only what is
specific to Claude Code.

@AGENTS.md

## Claude Code specifics

- **Template markers.** A `<!-- template-example: … -->` (or
  `# template-example: …`) comment marks a passage about the bundled example
  package; after adoption, rewrite it from the new code (see the top of
  `AGENTS.md`).
- **Reuse first.** Search `docs/api/capabilities.md` (every public name in
  the package) before writing a helper; the "Reuse before you write" table in
  `AGENTS.md` maps the usual hand-rolled code to what already exists.
- **Partial test runs** need `--no-cov` (`addopts` turns coverage on and its
  90 % gate fails any subset).
- **GitHub.** When the `gh` CLI is unavailable, use the GitHub MCP tools for
  the same operations (PRs, issues, review threads, check runs).
