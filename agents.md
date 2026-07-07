---
title: Agent Notes
type: agent-guide
status: active
updated: 2026-07-04
---

# Agent Notes

This workspace is a save folder for **The Farmer Was Replaced**. Treat it as an in-game Python-like codebase, not normal Python.

## Read First

- Read `docs/research.md` before planning endgame work.
- Read `docs/plan.md` for the existing strategy outline, but prefer `docs/research.md` when the two disagree.
- Check `save.json` for the current unlock/resource state before making progression assumptions.
- Use `__builtins__.py` as the local reference for available game functions, entities, items, hats, and unlocks.

## Important Strategy Context

- Do not assume 9x9 is endgame. This save currently has `expand_9`, but researched endgame strategies target 32x32 and 32-drone-capable automation.
- Write farm logic with `get_world_size()` and `max_drones()` unless a file is explicitly a benchmark or debug script for a fixed size.
- Current major missing progression targets include max expansion/drone/speed tiers, dinosaur/bones, and leaderboards.
- Top-tier endgame work is algorithmic: sunflower max-petal selection, pumpkin synchronization, cactus sorting, maze pathfinding/reuse, dinosaur safe pathing, and multi-drone ownership.

## Codebase Shape

Existing modules:

- `main.py`: current dispatcher.
- `farming.py`: shared till/water/harvest/resource helpers.
- `movement.py`: movement helpers.
- `poly.py`: polyculture/base resource loop.
- `pumpkin.py`: pumpkin loop.
- `maze.py`: maze/gold loop.

Recommended future modules:

- `sunflower.py`
- `cactus.py`
- `dinosaur.py`
- `unlocking.py`
- `benchmark.py`

## Development Guidance

- Preserve the small modular style already present.
- Keep resource thresholds named and centralized.
- Gate mechanics behind unlock checks before calling their functions/entities.
- Prefer lane or block ownership for spawned drones so workers do not collide or duplicate work.
- Use `simulate()`, `get_tick_count()`, and small `set_world_size()` test runs for benchmarking, but do not treat `set_world_size()` as permanent progression.
- Avoid broad rewrites unless the dispatcher or shared helpers are the actual task.
