---
title: Advanced Maze Modes Design
type: design-note
status: active
updated: 2026-07-04
source_task: task-11-advanced-maze-design
---

# Advanced Maze Modes Design

Current `maze.py` is intentionally simple: create a maze if safe, then use a left-hand wall follower until treasure is found. Keep that baseline as the fallback while adding advanced modes one at a time.

## Current Baseline

Mode: `wall_follow`

Flow:

1. If already on hedge or treasure, continue.
2. Otherwise plant a bush and spend weird substance only if the reserve guard passes.
3. Follow the left wall from `North`.
4. Harvest treasure when reached.

State needed:

- current facing direction
- current tile entity
- weird substance cost from `get_maze_substance_needed()`

Strengths:

- Small and reliable.
- No graph memory.
- Good fallback for any maze size.

Weaknesses:

- Can waste a lot of movement.
- Does not use `measure()` treasure coordinates.
- Does not support multi-drone search.

Failure cases:

- Calling the solver when no maze exists. Task 05 guarded this by making `setup_maze()` return `False`.
- Spending below weird substance reserve. Task 05 guarded this with `farming.item_above_reserve()`.

## Mode 1: Measured Treasure Pathfinding

Goal: use `measure()` to get the treasure coordinate, map the maze, and move by shortest known path instead of wall-following blindly.

Expected flow:

1. Ensure maze exists with the current `setup_maze()` guard.
2. Call `measure()` to get treasure position.
3. Explore reachable cells and record open directions with `can_move(direction)`.
4. Use BFS over the discovered graph to choose a route to the treasure.
5. Move along the route.
6. Harvest treasure.
7. Fall back to wall-follow if mapping fails.

State needed:

- `treasure_pos`
- `visited` set or dictionary keyed by `(x, y)`
- adjacency dictionary: `(x, y) -> list of neighbor positions`
- queue/list for BFS
- predecessor map for reconstructing the path
- current drone direction only if movement cost is later optimized

Implementation boundaries:

- First version can fully explore the maze before routing.
- Later version can stop exploring once treasure is reached.
- Keep this single-drone until the state model is proven.

Failure cases:

- `measure()` returns `None` because there is no active maze.
- Graph mapping misses a wrap or coordinate due to movement assumptions.
- The drone gets moved by helper functions and current position state becomes stale.
- BFS path is empty; fallback to wall-follow.

Resource costs:

- Same weird substance cost as baseline.
- Extra ticks for mapping.
- Likely lower movement cost on large mazes once pathing works.

Acceptance for implementation:

- Can solve at current world size.
- Falls back to `solve_maze(North)` if measured mode cannot produce a path.
- Does not change maze creation policy.

## Mode 2: Maze Reuse

Goal: avoid creating a fresh maze every time when the game mode allows extending or reusing the current maze/treasure state.

Expected flow:

1. Solve to treasure.
2. Before harvesting, decide whether to spend weird substance on the treasure or related maze mechanic.
3. If reuse succeeds, continue solving from the current maze state.
4. If reuse fails or reserve is too low, harvest and return to dispatcher.

State needed:

- current treasure position
- weird substance reserve and cost
- count of reuse attempts
- fallback harvest behavior

Implementation boundaries:

- Do not combine reuse with multi-drone in the first version.
- Add a hard cap per call so the dispatcher can regain control.
- Keep reserve protection stronger than baseline because reuse can spend repeatedly.

Failure cases:

- Spending weird substance below reserve.
- Infinite reuse loop that starves other resources.
- Reuse mechanic differs by unlock/achievement context.

Resource costs:

- Potentially high weird substance burn.
- Better gold per setup if reuse is valid.

Acceptance for implementation:

- Reuse is behind `ENABLE_MAZE_REUSE`.
- Dispatcher remains responsive.
- Weird substance reserve is never crossed.

## Mode 3: Multi-Drone Or Partitioned Maze

Goal: improve large-farm maze throughput once the farm approaches 32x32 and enough drones are available.

Two candidate approaches:

- Single large maze, distributed search: spawn workers at different entry lanes/sectors and let the first treasure finder trigger harvest.
- Partitioned mazes: split the field into smaller blocks, such as 8x8, with a worker or worker group per block.

State needed:

- worker assignment: row, column, or block
- shared discovery/completion signal
- whether treasure has been found
- per-worker path or wall-follow state
- safe way to stop helpers after harvest

Implementation boundaries:

- Do not start here. Build measured single-drone pathfinding first.
- Use `max_drones()` and `get_world_size()`.
- Keep the main drone useful as either coordinator or assigned worker.

Failure cases:

- Multiple drones spending setup resources at the same time.
- Workers entering each other's sectors without a shared stop signal.
- Main drone harvesting while helpers are still moving unpredictably.
- `max_drones()` being lower than expected at current unlock level.

Resource costs:

- Same or higher weird substance cost depending on one large maze versus many partitions.
- More parallel movement, but more coordination complexity.

Acceptance for implementation:

- Disabled behind an explicit flag.
- Proves one deterministic worker assignment before adding dynamic search.
- Can recover cleanly to dispatcher after treasure harvest.

## Recommended Implementation Order

1. Keep `wall_follow` as default.
2. Add `ENABLE_MEASURED_MAZE = False`.
3. Implement measured single-drone mapping and BFS behind the flag.
4. Benchmark against wall-follow with `benchmark.py`.
5. Add reuse behind a separate flag only after measured mode is stable.
6. Design multi-drone search only after max-drone behavior is understood in this save.

## Next Implementation Task

Create a new task for measured single-drone pathfinding:

- add `measure_treasure()`
- add `record_neighbors()`
- add `build_maze_graph()`
- add `find_path_to_treasure()`
- add `follow_path(path)`
- fallback to current `solve_maze(North)`

The current `maze.py` should not be rewritten wholesale. Add one mode at a time.
