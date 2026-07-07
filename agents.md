---
title: Agent Notes
type: agent-guide
status: active
updated: 2026-07-08
---

# Agent Notes

This workspace is a save folder for **The Farmer Was Replaced**. Treat it as an in-game Python-like codebase, not normal Python.

## Read First

- Read `docs/strategy/README.md` for the live implementation state before reviewing code.
- Read `docs/research.md` for broader endgame context when planning larger strategy changes.
- Check `save.json` for the current unlock/resource state before making progression assumptions.
- Use `__builtins__.py` as the local reference for available game functions, entities, items, hats, and unlocks.

## Important Strategy Context

- Do not assume 9x9 is endgame. Researched endgame strategies target 32x32 and 32-drone-capable automation.
- Write farm logic with `get_world_size()` and `max_drones()` unless a file is explicitly a benchmark or debug script for a fixed size.
- Dinosaurs/bones are now unlocked and active. Current major future targets include safer dinosaur routing, maze pathfinding/reuse, benchmarking, and leaderboards.
- Top-tier endgame work is algorithmic: sunflower max-petal selection, pumpkin synchronization, cactus sorting, maze pathfinding/reuse, dinosaur safe pathing, and multi-drone ownership.

## Codebase Shape

Existing modules:

- `main.py`: current dispatcher.
- `targets.py`: low/high item targets.
- `drones.py`: shared spawned-drone task helper.
- `farming.py`: shared till/water/harvest/replace helpers.
- `movement.py`: movement helpers.
- `poly_drones.py`: staggered worker starts for base resources.
- `poly_basic.py`: polyculture/base resource loop.
- `sunflower.py`: max-petal power loop.
- `pumpkin.py`: pumpkin loop.
- `cactus.py`: cactus sort/harvest loop.
- `maze_basic.py`: single-maze creation and wall follower.
- `maze_drones.py`: partitioned maze/gold loop.
- `dinosaur.py`: current bone loop.

Recommended future modules:

- `unlocking.py`
- `benchmark.py`

## Development Guidance

- Preserve the small modular style already present.
- Keep resource targets named and centralized in `targets.py`.
- Gate mechanics behind unlock checks before calling their functions/entities.
- Prefer lane or block ownership for spawned drones so workers do not collide or duplicate work.
- Use `simulate()`, `get_tick_count()`, and small `set_world_size()` test runs for benchmarking, but do not treat `set_world_size()` as permanent progression.
- Avoid broad rewrites unless the dispatcher or shared helpers are the actual task.
