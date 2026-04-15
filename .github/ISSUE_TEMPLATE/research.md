---
name: Research / Comparative Analysis
about: Investigate an external repo, paper, or prior art and map it onto this project. Produces a prioritized roadmap of follow-up issues.
title: "research: <short topic>"
labels: ["type:research"]
---

<!--
Research issues are for structured investigation that produces a plan, not
code. Typical shapes:
  - Compare an external codebase / paper against this project
  - Survey prior art and extract what's worth adopting
  - Benchmark alternative approaches before committing to a design

The output is an inventory + gap analysis + prioritized list of follow-up
issues (features / designs / chores). Those follow-up issues do the actual
work and should link back here.
-->

## Context
<!--
What are we investigating and why? One or two paragraphs. Include the
motivating question and what decision / roadmap this research will inform.
-->

## Scope & Questions
<!-- The concrete questions this research will answer. -->
- [ ] <question 1>
- [ ] <question 2>

## Sources Surveyed
<!-- Repos, papers, docs, discussions. Link everything. -->
- <repo or paper>: `<url>` — <one-line description>
- <repo or paper>: `<url>` — <one-line description>

---

## Findings — What `<subject>` Provides
<!-- Inventory of the thing being studied. Use the structures below only if
     they fit; delete subsections that don't apply. -->

### Package / Project Structure
```
<tree or component map>
```

### Core Data Structures
| Structure | Fields | Purpose |
|---|---|---|
| `<name>` | `<fields>` | <role> |

### Core Algorithms / Features
#### A. <Algorithm or feature area>
- `<function or symbol>` — <what it does, complexity, assumptions>
- ...

#### B. <Algorithm or feature area>
- ...

---

## Comparison — What This Project Already Has
<!-- Direct equivalents. Be specific — cite file paths + function names. -->

| Subject's Feature | This Project's Equivalent | Path | Notes |
|---|---|---|---|
| <feature> | `<our name>` | `src/<path>` | <gap or divergence> |

---

## Gap Analysis

### A. Present here but missing enhancements from `<subject>` (HIGH / MED / LOW)
#### A1. <Enhancement name> (PRIORITY)
- **`<subject>`**: <what it does differently>
- **This project**: <current state>
- **What's needed**: <concrete change>
- **Impact**: <why it matters>

### B. Completely missing from this project
#### B1. <Feature name> (PRIORITY)
- **What it is**: <description>
- **Why useful**: <motivation>
- **Where in this project**: <proposed module / file>

### C. We have it, subject doesn't (context only — no action)
<!-- Useful for reassuring ourselves we haven't regressed on something. -->
- `<our feature>` — <why the subject doesn't need it>

---

## Summary Table
| Feature | Subject | This project | Status |
|---|---|---|---|
| <feature> | ✓ | ✗ | **Missing** |
| <feature> | ✓ | ✓ (partial) | **Enhancement needed** |
| <feature> | ✗ | ✓ | We're ahead |

---

## Recommended Integration Priority
<!-- Phased roadmap. Each phase should be shippable on its own. -->

### Phase 1: Foundations
1. <item>
2. <item>

### Phase 2: <theme>
3. <item>

### Phase 3: <theme>
4. <item>

---

## Proposed Follow-up Issues
<!-- Concrete issues to open from this research. These are what actually
     get done. Link them back to this issue via `Parent research: #<this>`. -->

- [ ] `feat(<scope>): <title>` — covers Phase 1 item 1
- [ ] `feat(<scope>): <title>` — covers Phase 1 item 2
- [ ] `[Design] <title>` — resolves <open question>

---

## Key Synergies (optional)
<!-- Narrative section for cross-cutting observations: how combining X and
     Y unlocks Z, architectural implications, dependency chains. Delete if
     not useful. -->

---

## References
- <paper / repo / doc> — `<url>`
- <paper / repo / doc> — `<url>`

## Relationships
- Parent (theme epic, if any): #
- Blocked by: #
- Blocks (follow-up issues may reference this): #
- Related: #
