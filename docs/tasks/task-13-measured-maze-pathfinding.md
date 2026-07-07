---
title: "Task 13: Add Measured Maze Pathfinding"
type: task
status: complete
order: 13
phase: specialist-loop
depends_on:
  - task-11-advanced-maze-design
updated: 2026-07-04
completed_on: 2026-07-04
notes: "Adds measured treasure targeting with heuristic DFS and wall-follow fallback. This is the first real maze upgrade, not the final multi-drone endgame solver."
---

# Task 13: Add Measured Maze Pathfinding

## Goal

Improve maze solving beyond blind wall-following by using `measure()` and `can_move()`.

## Files

- `maze.py`
- `docs/tasks/README.md`

## Work

- Add a measured maze mode behind a flag.
- Use `measure()` to locate treasure.
- Track visited coordinates.
- Prefer legal moves that reduce wrapped distance to treasure.
- Backtrack when no unvisited legal move is available.
- Keep wall-following as fallback.

## Acceptance

- Current maze creation policy stays guarded.
- Measured mode can be disabled with a flag.
- Solver no longer relies only on wall-following.
- Syntax check passes.
