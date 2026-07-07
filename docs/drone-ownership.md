---
title: Drone Ownership Notes
type: design-note
status: active
updated: 2026-07-04
---

# Drone Ownership Notes

This save currently mixes row-based drone work with single-drone specialist baselines. Future 32x32 work should preserve clear ownership so drones do not duplicate work or fight over the same tile.

## Current Loops

| Module | Current ownership | Notes |
| --- | --- | --- |
| `poly.py` | row ownership | Each spawned worker receives one `y` row and walks across `x`. |
| `pumpkin.py` | row ownership per pass | Each spawned worker receives one `y` row for each pumpkin pass. |
| `sunflower.py` | full-field single drone | Disabled by default because the baseline scan is disruptive in live play. |
| `cactus.py` | full-field single drone | Disabled by default until the sorter is deliberately tested. |
| `maze.py` | single active solver | Advanced maze work should be designed before adding multiple drones. |

## Intended Direction

- Keep row ownership for simple row-major crop passes.
- Consider column ownership for pumpkins if 32x32 synchronization becomes easier that way.
- Use block ownership for future maze partitioning and possible cactus experiments.
- Let the main drone either own a lane or coordinate harvest/unlock decisions; do not leave it idle by default.

## Rules

- Do not assume `max_drones() == get_world_size()`.
- Spawned workers should receive an explicit row, column, or block.
- Full-field specialist loops should be opt-in until benchmarked.
- Shared `world` updates need clear ownership or coordinator logic.
