---
title: "Task 11: Design Advanced Maze Modes"
type: task
status: complete
order: 11
phase: design
depends_on:
  - task-05-maze-reserves
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 11: Design Advanced Maze Modes

## Goal

Plan advanced maze work before replacing the safe wall follower.

## Files

- `docs/maze-design.md`
- optionally `maze.py` comments only.

## Work

- Document three maze modes:
  - baseline wall-follow
  - measured treasure pathfinding
  - reuse or multi-drone/partitioned maze mode
- Identify what state each mode needs.
- Identify failure cases and resource costs.
- Do not implement advanced pathfinding in this task.

## Dependencies

- Task 05 recommended.

## Acceptance

- The next maze implementation task has a clear design.
- Current `maze.py` behavior remains unchanged.
