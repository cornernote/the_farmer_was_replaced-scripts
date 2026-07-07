---
title: Save0 Automation Notes
type: readme
status: active
updated: 2026-07-08
---

# Save0 Automation Notes

This folder is a save/code workspace for **The Farmer Was Replaced**. The code is the game's Python-like language, not normal Python, so use `__builtins__.py` as the local reference for supported functions and game entities.

## Where To Start

- [Agent notes](agents.md): rules for future code reviews and edits.
- [Current strategies](docs/strategy/README.md): live strategy index and dispatcher order.
- [Research](docs/research.md): broader endgame context and strategy background.
- [Benchmarking](docs/benchmarking.md): guidance for future measurement helpers.

## Current Strategy Files

- [Dispatcher](docs/strategy/dispatcher)
- [Sunflower / power](docs/strategy/sunflower)
- [Polyculture / base resources](docs/strategy/polyculture)
- [Pumpkin](docs/strategy/pumpkin)
- [Cactus](docs/strategy/cactus)
- [Maze / gold](docs/strategy/maze)
- [Dinosaur / bones](docs/strategy/dinosaur)

## Code Shape

- `main.py`: target-driven dispatcher.
- `targets.py`: low/high item targets.
- `drones.py`: shared spawned-drone task helper.
- `farming.py`: shared harvest/till/water/replace helpers.
- `movement.py`: movement helpers.
- `poly_drones.py` and `poly_basic.py`: base-resource polyculture loop.
- `sunflower.py`: measured max-petal power loop.
- `pumpkin.py`: row-worker pumpkin loop.
- `cactus.py`: cactus sort/harvest loop.
- `maze_basic.py` and `maze_drones.py`: maze gold loops.
- `dinosaur.py`: current bone loop.

## Current Priorities

- Benchmark the polyculture 8-neighbor waiting loop.
- Add safer dinosaur pathing before leaderboard-style bone farming.
- Add benchmark helpers only when comparing strategies, not inside the live dispatcher.

## Conventions

- Use `get_world_size()` and `max_drones()` in production logic.
- Keep strategy docs updated when changing strategy behavior.
- Treat `set_world_size()` as a test/debug tool, not permanent progression.
- Keep modules small and focused; avoid broad rewrites unless shared helpers or the dispatcher are the actual target.
