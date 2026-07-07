---
title: "Task 04: Add Baseline Sunflower Power Loop"
type: task
status: complete
order: 4
phase: specialist-loop
depends_on:
  - task-01-resource-reserves
  - task-02-dispatcher-jobs
updated: 2026-07-04
completed_on: 2026-07-04
notes: "Baseline module exists, but automatic dispatcher job is disabled by default after live testing showed the single-drone full-field scan was too disruptive."
---

# Task 04: Add Baseline Sunflower Power Loop

## Goal

Add a correct single-drone sunflower loop that measures petals and harvests max-petal flowers for power.

## Files

- `sunflower.py`
- `main.py`
- `farming.py`

## Work

- Create `sunflower.py`.
- Plant/till/water sunflowers across `get_world_size()`.
- Measure petals with `measure()`.
- Track max-petal position(s).
- Harvest only max-petal flowers when harvestable.
- Replant harvested tiles.
- Add a dispatcher job gated by sunflower unlock and `need_power()`.

## Dependencies

- Task 01.
- Task 02.

## Acceptance

- If power is low, dispatcher can run sunflower.
- If sunflower is locked, dispatcher skips it.
- No fixed-size field logic.
- Existing poly/maze/pumpkin fallback remains intact.
