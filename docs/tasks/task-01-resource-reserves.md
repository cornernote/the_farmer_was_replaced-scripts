---
title: "Task 01: Centralize Resource Reserves"
type: task
status: complete
order: 1
phase: stabilize
depends_on: []
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 01: Centralize Resource Reserves

## Goal

Move resource thresholds into one place so future dispatcher and unlock work can share the same reserve policy.

## Files

- `farming.py`

## Work

- Add named minimum/preferred reserve constants or simple getter functions.
- Include hay, wood, carrot, pumpkin, water, fertilizer, weird substance, power, gold, cactus, and bone.
- Add helper checks:
  - `need_power()`
  - `need_gold()`
  - `need_base_materials()`
  - `need_pumpkin_stock()`
  - `item_above_reserve(item, amount)`
- Keep existing function names working where possible so `main.py` does not break.

## Dependencies

- None.

## Acceptance

- Existing `main.py` still runs with the old loop selection.
- No specialist module is required yet.
- No fixed 9x9 assumptions are introduced.
