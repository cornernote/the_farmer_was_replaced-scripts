---
title: "Task 02: Refactor Dispatcher To Jobs"
type: task
status: complete
order: 2
phase: stabilize
depends_on:
  - task-01-resource-reserves
updated: 2026-07-04
completed_on: 2026-07-04
---

# Task 02: Refactor Dispatcher To Jobs

## Goal

Replace the chained `if/elif` in `main.py` with a small job selector while preserving current behavior.

## Files

- `main.py`
- `farming.py`

## Work

- Add a `select_job()` function in `main.py`.
- Represent jobs with small dictionaries or simple functions.
- Initially include only existing runnable jobs:
  - maze/gold
  - polyculture/base resources
  - pumpkin stock
- Keep world creation lazy and only rebuild when switching to a crop loop.
- Do not add sunflower/cactus/dinosaur calls yet unless stubs already exist.

## Dependencies

- Task 01.

## Acceptance

- Existing maze, polyculture, and pumpkin flows still run.
- The dispatcher is easier to extend with new jobs.
- No locked mechanic is called.
