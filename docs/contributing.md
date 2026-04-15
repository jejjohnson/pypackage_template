# Contributing

This page documents the label taxonomy, epic model, and issue conventions used in this project.

---

## Label Taxonomy

Every issue carries exactly one `type:*`, one or more `area:*`, at most one `layer:*`, one `wave:*`, and one `priority:*`.

| Scope | Labels |
|---|---|
| **Type** | `type:epic-wave`, `type:epic-theme`, `type:feature`, `type:design`, `type:chore`, `type:docs`, `type:bug`, `type:research` |
| **Area** | `area:engineering`, `area:testing`, `area:docs`, `area:code` — extend per project (e.g. `area:algorithmic`, `area:integration`) |
| **Layer** | `layer:0-primitives`, `layer:1-components`, `layer:2-models` — only if the project has a formal layer stack |
| **Wave** | `wave:0`, `wave:1`, `wave:2`, … — release-scoped phases (add `wave:N-<slug>` variants for descriptive labels) |
| **Priority** | `priority:p0` (blocker), `priority:p1` (high), `priority:p2` (normal) |

Bootstrap the standard set on a fresh repo:

```bash
make gh-labels
```

The script lives at `.github/scripts/create-labels.sh`. Edit the hard-coded `create …` entries in the script to customise `area:*`, `layer:*`, and `wave:*` for the project, then re-run — the script is idempotent.

---

## Two-Layer Epic Model

Work is organised as **Wave → Theme → Issue**:

```
[EPIC] Wave N   (L1)   —   release-scoped mega-epic, owns a milestone
  ├── [EPIC] <theme>   (L2)   —   parallel-safe group of issues
  │     ├── feature / design / chore / bug issue
  │     └── …
  └── [EPIC] <theme>   (L2)
        └── …
```

- **Wave epic** (`type:epic-wave`) maps one-to-one with a milestone (`vX.Y-<slug>`). Groups several Theme epics that can run in parallel.
- **Theme epic** (`type:epic-theme`) groups concrete issues that ship together as a coherent slice. Themes inside a wave are parallel-safe unless the body says otherwise.
- **Issue** (feature / design / chore / bug) is the leaf — a single substantial deliverable that rolls up to a Theme epic.

Stragglers are discouraged: any `type:feature` issue should attach to a Theme epic. If no suitable theme exists, create one first.

---

## Issue Format

Issue templates live in `.github/ISSUE_TEMPLATE/`:

| Template | When to use |
|---|---|
| `Epic — Wave (L1)` | Opening a new release-scoped wave |
| `Epic — Theme (L2)` | Grouping related issues inside a wave |
| `Feature / Enhancement` | One substantial deliverable |
| `Design / ADR` | Resolve an open design question for a new API |
| `Bug report` | Something isn't working |
| `Research / Comparative Analysis` | Study prior art (external repo, paper) and produce a prioritized roadmap of follow-up issues |

Feature + Design templates include two **optional** sections for context-heavy issues:

- **Design Snapshot** — paste API sketches, code examples, or excerpts from private / external design docs so the issue is self-contained.
- **Mathematical Notes** — equations, sign conventions, numerical considerations.

Delete either section if not relevant. Both exist so that an implementer (human or AI agent) can work on the issue without opening other repos or channels.

---

## Drafting a wave backlog

For large planning exercises (new wave, new release, large refactor), draft the whole backlog as one markdown file **before** opening GitHub issues. A template lives at [`docs/templates/wave-backlog.md`](templates/wave-backlog.md).

Why:

- **Review the whole wave in one scroll** instead of clicking through 15 half-drafted issues
- **Share context once** at the top (Shared Context · Design Snapshot · Intended Package Layout · Runtime Boundary) rather than duplicating across every child issue
- **Stable draft IDs** (`<PREFIX>-01`, `<PREFIX>-02`, …) let child issues reference each other before GitHub issue numbers exist

Workflow:

1. Copy `docs/templates/wave-backlog.md` into your project's `.plans/` directory (gitignored). Rename to describe the wave — e.g. `.plans/wave-1-backlog.md`.
2. Pick a short project prefix (e.g. `PYX` for pyrox, `OBX` for optax_bayes). Number drafts sequentially.
3. Fill in shared context at the top, then draft each issue body.
4. When the file is ready, open each draft as a real GitHub issue using the matching `.github/ISSUE_TEMPLATE/`. Copy the body verbatim.
5. Record GitHub issue numbers next to draft IDs in the backlog file, or replace draft IDs throughout. Update cross-references.
6. Either delete the backlog file or archive it in `.plans/archive/`.

---

## Relationships

Use an explicit `## Relationships` block at the bottom of each issue / epic body:

```markdown
## Relationships
- Parent: #<theme-epic>
- Blocked by: #
- Blocks: #
- Related: #
```

GitHub's task-list feature links bidirectionally from the parent, so checklist items in a Theme epic body auto-show in the referenced issues.

---

## Pre-commit checklist

Run these locally before opening a PR:

```bash
make format       # ruff format . + ruff check --fix .   (applies changes)
make lint         # ruff check .                         (CI-style check)
make typecheck    # ty check
make test         # pytest
```

Note that `make format` **mutates files** — it formats and applies autofixes. `make lint` is the CI-parity read-only check. Run `make format` first, commit the result, then run `make lint` / `make test` to verify.

Pre-commit hooks run ruff on every commit. Run `make precommit` to apply them to all files manually.

Commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/) specification — enforced on PR titles by `.github/workflows/conventional-commits.yml`.
