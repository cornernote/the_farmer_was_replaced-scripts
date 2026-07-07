---
title: "Task 09: Document Drone Ownership Patterns In Code"
type: task
status: complete
order: 9
phase: scaling
depends_on:
  - task-02-dispatcher-jobs
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 09: Document Drone Ownership Patterns In Code

## Goal

Prepare multi-drone scaling by making ownership assumptions explicit before deeper rewrites.

## Files

- `poly.py`
- `pumpkin.py`
- `sunflower.py` if present
- `cactus.py` if present
- optional `docs/drone-ownership.md`

## Work

- Identify whether each loop uses row, column, or full-field ownership.
- Add small comments or helper names where ownership is unclear.
- If creating `docs/drone-ownership.md`, describe current ownership and intended 32x32 direction.
- Do not rewrite drone scheduling in this task.

## Dependencies

- Task 02 recommended.

## Acceptance

- Future agent can see which drone owns what.
- No behavior changes required.
- Main loop remains runnable.
