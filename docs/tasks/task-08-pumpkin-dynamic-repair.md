---
title: "Task 08: Make Pumpkin Loop More Dynamic"
type: task
status: complete
order: 8
phase: specialist-loop
depends_on:
  - task-01-resource-reserves
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 08: Make Pumpkin Loop More Dynamic

## Goal

Improve pumpkin reliability without redesigning the whole loop around drones yet.

## Files

- `pumpkin.py`
- `farming.py` if helper changes are needed.

## Work

- Replace fixed pass assumptions where practical with checks for dead pumpkins and maturity.
- Preserve immediate dead-pumpkin repair.
- Avoid using fertilizer below the shared fertilizer reserve.
- Keep current row-drone structure unless a small, safe cleanup is obvious.

## Dependencies

- Task 01.

## Acceptance

- Pumpkin loop still plants, repairs, and harvests.
- Fertilizer reserve is protected.
- No fixed-size assumptions are added.
