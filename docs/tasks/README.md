---
title: Task Index
type: task-index
status: active
plan: docs/plan.md
updated: 2026-07-04
---

# Task Index

These tasks break `docs/plan.md` into small implementation chunks. Each task should leave the bot runnable when complete.

Recommended order:

1. `task-01-resource-reserves.md`
2. `task-02-dispatcher-jobs.md`
3. `task-03-unlock-guards.md`
4. `task-04-sunflower-baseline.md`
5. `task-05-maze-reserves.md`
6. `task-06-benchmark-helpers.md`
7. `task-07-cactus-baseline.md`
8. `task-08-pumpkin-dynamic-repair.md`
9. `task-09-drone-ownership-notes.md`
10. `task-10-dinosaur-gated-stub.md`
11. `task-11-advanced-maze-design.md`
12. `task-12-leaderboard-simulation-harness.md`
13. `task-13-measured-maze-pathfinding.md`

Rules for every task:

- Keep code runnable after the task.
- Use `get_world_size()` and `max_drones()` for production logic.
- Gate locked mechanics before use.
- Prefer small, reversible edits over broad rewrites.
- Update this index if tasks are added, removed, or reordered.
