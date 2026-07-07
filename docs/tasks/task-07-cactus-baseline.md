---
title: "Task 07: Add Baseline Cactus Sort Farm"
type: task
status: complete
order: 7
phase: specialist-loop
depends_on:
  - task-01-resource-reserves
  - task-02-dispatcher-jobs
  - task-03-unlock-guards
updated: 2026-07-04
completed_on: 2026-07-04
notes: "Baseline module and gated dispatcher job exist, but ENABLE_CACTUS_JOB defaults to False until the sorter has been tested deliberately."
---

# Task 07: Add Baseline Cactus Sort Farm

## Goal

Add a correct cactus plant/sort/harvest loop using dynamic world size.

## Files

- `cactus.py`
- `main.py`
- `farming.py`

## Work

- Create `cactus.py`.
- Plant cactus across the field with soil/water handling.
- Wait or loop until cactus tiles are ready enough to sort/harvest.
- Implement a simple neighbor-swap sorter, preferably cocktail-shaker style.
- Harvest only after a pass completes with no swaps.
- Add dispatcher job gated by cactus unlock and cactus reserve need.

## Dependencies

- Task 01.
- Task 02.
- Task 03 recommended for unlock gating.

## Acceptance

- Cactus job is skipped if cactus is locked.
- Cactus loop works at current world size.
- Sorting uses `measure()` and `swap()`.
- No leaderboard optimization required.
