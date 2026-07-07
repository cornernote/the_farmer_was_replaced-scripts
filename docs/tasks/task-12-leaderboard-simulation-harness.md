---
title: "Task 12: Add Simulation And Leaderboard Harness"
type: task
status: complete
order: 12
phase: tooling
depends_on:
  - task-06-benchmark-helpers
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 12: Add Simulation And Leaderboard Harness

## Goal

Prepare repeatable testing after progression automation is stable.

## Files

- `benchmark.py`
- optional `leaderboard.py`

## Work

- Add helpers for `simulate()` experiments.
- Add a guarded wrapper for `leaderboard_run()`.
- Ensure leaderboard calls are not made automatically from `main.py`.
- Document how to run a manual benchmark or leaderboard attempt.

## Dependencies

- Task 06.
- Stable specialist loops for whatever is being benchmarked.

## Acceptance

- Simulation/leaderboard helpers exist but are opt-in.
- Main progression loop does not accidentally start leaderboard runs.
