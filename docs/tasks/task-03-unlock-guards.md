---
title: "Task 03: Add Unlock Guards And Safe Afford Checks"
type: task
status: complete
order: 3
phase: stabilize
depends_on:
  - task-01-resource-reserves
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 03: Add Unlock Guards And Safe Afford Checks

## Goal

Create a small unlock helper module that can be used later without changing crop modules.

## Files

- `unlocking.py`
- `main.py` only if needed for import smoke-checking.

## Work

- Add `has_unlock(unlock)` wrapper around `num_unlocked()`.
- Add `cost_of(unlock)` wrapper around `get_cost()`.
- Add `can_afford_without_reserve(cost)` using reserve helpers from `farming.py`.
- Add `can_unlock_safely(unlock)`.
- Do not call `unlock()` automatically yet.

## Dependencies

- Task 01.

## Acceptance

- New module imports cleanly in-game.
- No resource spending behavior changes yet.
- Locked future mechanics can be checked safely.
