---
title: "Task 05: Protect Maze Weird Substance And Raise Gold Target"
type: task
status: complete
order: 5
phase: specialist-loop
depends_on:
  - task-01-resource-reserves
  - task-02-dispatcher-jobs
updated: 2026-07-04
completed_on: 2026-07-04
notes: "Maze setup is guarded and reserve-mode gold farming exists behind ENABLE_GOLD_RESERVE_JOB, but the live dispatcher defaults to the legacy gold threshold after testing showed reserve-mode maze farming was too disruptive."
---

# Task 05: Protect Maze Weird Substance And Raise Gold Target

## Goal

Make maze/gold farming safer without replacing the existing solver.

## Files

- `maze.py`
- `farming.py`
- `main.py` if job thresholds need wiring.

## Work

- Raise the gold minimum from the old low threshold to the shared reserve.
- Before creating a maze, check the weird substance cost.
- If there is not enough weird substance above reserve, skip maze setup and let dispatcher choose another job.
- Keep the current wall-following solver.

## Dependencies

- Task 01.
- Task 02.

## Acceptance

- Maze loop does not consume the last weird substance reserve.
- Gold farming still works with the current solver.
- No pathfinding rewrite in this task.
