---
title: "Task 10: Add Gated Dinosaur Stub"
type: task
status: complete
order: 10
phase: future-gated
depends_on:
  - task-02-dispatcher-jobs
  - task-03-unlock-guards
updated: 2026-07-04
completed_on: 2026-07-04
notes: "Stub and dispatcher entry are double-gated by ENABLE_DINOSAUR_JOB and Unlocks.Dinosaurs; no hat switching or movement yet."
---

# Task 10: Add Gated Dinosaur Stub

## Goal

Prepare for dinosaur/bone work without activating it before unlock.

## Files

- `dinosaur.py`
- `main.py`
- `unlocking.py` if present.

## Work

- Create `dinosaur.py` with a no-op or simple `run()` that returns immediately if dinosaurs are locked.
- Add a dispatcher job only if it is fully gated by `num_unlocked(Unlocks.Dinosaurs)`.
- Do not switch hats or move unless unlocked.
- Add comments for the later Hamiltonian/serpentine route.

## Dependencies

- Task 02.
- Task 03 recommended.

## Acceptance

- No behavior changes while dinosaurs are locked.
- Dispatcher can include future bone job safely.
- No apple/pathfinding logic yet.
