---
name: Epic — Theme (L2)
about: A parallel-safe group of issues under a Wave epic. See docs/contributing.md for the two-layer epic model.
title: "[EPIC] <theme title>"
labels: ["type:epic-theme"]
---

<!--
A Theme epic is the L2 container under a Wave. It groups several concrete
issues (features / designs / chores) that ship together as a coherent slice.
-->

## Theme
<!-- One-sentence theme / outcome for this group. -->

## Parent Wave
- Wave epic: #
- Wave label: `wave:N-<slug>`
- Milestone: `vX.Y-<slug>`

## Motivation
<!-- Why this group exists; what it ships together. -->

## Issues
- [ ] #<issue> — <short description>
- [ ] #<issue> — <short description>

## Parallelism
- Can run in parallel with: # (other theme epics in the same wave)
- Blocked by (inside this wave): #
- Must complete before: #

## Definition of Done
- [ ] All child issues closed
- [ ] Tests for the theme's surface land and pass
- [ ] Docs / API pages for the theme's surface land

## Relationships
- Parent: #<wave-epic>
- Related: #
