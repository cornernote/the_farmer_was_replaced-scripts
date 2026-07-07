---
title: The Farmer Was Replaced Endgame Research
type: research
status: active
researched_on: 2026-07-04
updated: 2026-07-04
---

# The Farmer Was Replaced Endgame Research

Research date: 2026-07-04

This note corrects the earlier mistake: this save is currently around 9x9 (`expand_9`), but 9x9 is not the endgame. Public endgame examples repeatedly target 32x32 farms with up to 32 drones, and the highest-tier strategies are less about generic farming and more about specialized algorithms for each late-game mechanic.

## Current Save State

From `save.json`:

- Current farm expansion unlock: `expand_9`.
- Current major unlocks: polyculture, pumpkins, sunflowers/power, cactus, mazes/gold, simulation, multi-drone, `set_world_size`, and wizard hat.
- Not yet visible in unlocks: dinosaurs/bones and leaderboards.
- Resource state at read time: very high hay/wood, several million carrots/pumpkins, large weird substance/water stock, low hundreds of gold, about 1k power.

Interpretation:

- This is late-midgame, not endgame.
- The next strategic bridge is maxing expansion/drone/speed/crop tiers, improving gold and power generation, then adding cactus and dinosaur/bone systems.
- The code should be written using `get_world_size()` and `max_drones()` rather than fixed 9x9 assumptions.

## How The Game Works At High Level

The game is a programming/optimization idler where the drone automates farming, movement, harvesting, trading, unlocking, and later algorithmic puzzles. The late game adds mechanics that behave like classic CS problems:

- Polyculture: adaptive crop placement using `get_companion()`.
- Sunflowers: measurement/selection optimization.
- Pumpkins: full-field synchronization with dead-pumpkin repair.
- Cactus: grid sorting with neighbor swaps.
- Mazes: maze generation and pathfinding.
- Dinosaurs: snake/Hamiltonian-path routing.
- Megafarm: parallel work through spawned drones.
- Simulation/leaderboards: benchmarked, repeatable runs.

The local `__builtins__.py` confirms important mechanics:

- `Entities.Cactus`: cacti have sizes 0-9; adjacent sorted cacti harvest recursively; reward is based on harvested group size squared.
- `Entities.Pumpkin`: connected mature pumpkins become a mega pumpkin; harvested amount is the mega pumpkin size cubed; about one in five mature pumpkins dies.
- `Entities.Sunflower`: harvesting a max-petal sunflower with at least 10 sunflowers gives bonus power.
- `Entities.Treasure`: gives gold equal to maze side length.
- `measure()`: returns sunflower petals, treasure position in maze, cactus size, or dinosaur type depending on context.
- `max_drones()`, `spawn_drone()`, and `wait_for()` are the core megafarm tools.
- `set_world_size(size)` is for limiting/debugging the farm and clears/resets the field while the program runs.
- `leaderboard_run()` starts timed category runs once leaderboards are unlocked.

## Endgame Scale

Evidence from community posts and guides points to 32x32 as the practical max-scale target:

- A Reddit post discusses a player who upgraded to a 32x32 farm and had access to 32 drones, including the original drone.
- A 32x32 maze post describes spawning 31 helper drones plus the main drone to search a single large maze.
- Steam posts and community snippets discuss 32x32 pumpkin, maze, cactus, and dinosaur strategies.
- A Medium multi-drone guide explicitly frames giant pumpkin work around a 32x32 farm where each drone can own a column.

Research conclusion:

- Endgame code should be 32x32-safe.
- Strategies should avoid hard-coded 9, 16, or 32 except in dedicated benchmark files.
- The architecture should support both current-save progression and max-size leaderboard-style scripts.

## Top-Tier Strategy Patterns

### 1. Dispatcher And Resource Economy

Top automation is not one loop; it is a dispatcher that selects specialized loops based on shortages, unlock costs, and current goals.

Good dispatcher priorities:

1. Keep power above minimum.
2. Keep gold above minimum.
3. Keep base materials above minimum.
4. Farm the next unlock's bottleneck resource.
5. Run specialist loops only when they are profitable.
6. Benchmark loops with `get_tick_count()` or `simulate()`.

Avoid:

- Running one crop forever.
- Hard-coding current farm size.
- Spending gold/power/materials below reserve when unlocking.
- Letting spawned drones overlap without a stable ownership model.

### 2. Polyculture / Base Resources

Polyculture remains important in endgame because it is the recovery layer for hay, wood, carrot, and weird substance.

Strong pattern:

- Maintain a world model of target entities.
- On every harvested tile, call `get_companion()`.
- Update the world model at the companion's requested coordinate.
- Use drones by row or column, but make sure each drone owns a stable lane.

For weird substance:

- Fertilizer can infect plants and convert part of harvest yield to weird substance.
- A focused tree/bush loop with fertilizer plus companion planting is a good support loop for maze-heavy progress.

### 3. Sunflowers / Power

Sunflowers are not just "plant and harvest." They are a selection problem:

- Plant enough sunflowers.
- Measure petals.
- Harvest only a sunflower with the maximum petal count.
- Keep enough sunflowers alive to preserve the max-petal bonus condition.

Top pattern:

- Fill field with sunflowers.
- Store `(petals, x, y)` values.
- Identify max petals.
- Harvest max-petal positions when ready.
- Replant and repeat until power target is reached.

Reason this matters:

- Power affects throughput and unlocks.
- Current code only plants sunflowers when power is low; it does not intentionally choose max-petal harvests.

### 4. Pumpkins / Mega Pumpkin

Pumpkins are a synchronization problem:

- Every tile must be pumpkin.
- Dead pumpkins must be repaired.
- The field should be harvested only once the giant/mega pumpkin is mature.

Top pattern:

- One drone per column or row at 32x32.
- Each worker keeps its lane planted, watered, and repaired.
- The coordinator checks representative tiles, often comparing `measure()` values or checking corners, then harvests when the full mega pumpkin is connected.
- Replant immediately after harvest.

Community examples for 32x32 pumpkins emphasize that the naive full-field loop works but is not top-tier; drone lane ownership is the important upgrade.

### 5. Cactus / Sorting

Cactus is a sorting problem. The local builtin says adjacent sorted cacti harvest recursively and reward scales with harvested group size squared. Public guides and repos consistently describe cactus farms as neighbor-swap sorting algorithms.

Baseline correct strategy:

1. Plant cactus on all tiles.
2. Wait until grown.
3. Measure cactus sizes.
4. Sort the grid using `swap(direction)`.
5. Harvest once the grid is sorted.

Common algorithms:

- 2D bubble sort: easiest and reliable.
- Cocktail shaker sort: improves by sweeping both directions and shrinking the active range as edges become sorted.
- Insertion-style placement: can be faster when movement and swap costs are carefully managed.

Leaderboard clue:

- A Reddit cactus leaderboard discussion mentions restricting cocktail shaker sort ranges as a meaningful improvement, shaving noticeable time from a run.

Implementation implication:

- Start with simple row-major/cocktail sorting for correctness.
- Then optimize by avoiding repeated full-grid passes, reducing movement, and caching measured values only if the game mechanics make the cache trustworthy after swaps.

### 6. Mazes / Gold

Maze strategy has layers:

Baseline:

- Plant bush.
- Use `Items.Weird_Substance` to turn it into a maze.
- Follow a wall until treasure.
- Harvest treasure.

The current code already uses a left-hand wall follower. That is valid for simple loop-free mazes.

Better:

- Use `measure()` to get the treasure position.
- Map or remember maze connectivity.
- Pathfind to the treasure instead of wandering.
- Reuse mazes by applying weird substance to treasure before harvesting, where the goal/achievement allows it.

Top-tier / high-throughput patterns:

- 32x32 single maze with many drones distributed across the maze, first drone to find treasure triggers the next cycle.
- Partitioned 32x32 field with multiple smaller mazes, such as 8x8 blocks, each handled by its own drone or team. Steam discussion suggests multiple small mazes can approach the same gold as one 32x32 maze but faster if placement and movement are correct.
- For leaderboard-level maze runs, map the maze graph and move directly to `measure()`'s treasure coordinate.

Implementation implication:

- Keep the wall-follower as baseline.
- Add a maze module that can choose between:
  - simple wall-follow
  - multi-drone random/distributed search
  - mapped pathfinding/reuse mode

### 7. Dinosaurs / Bones

Dinosaurs are a snake/path-planning problem. Public writeups describe the safe baseline as a Hamiltonian-style route that visits the grid without self-collision.

Mechanic summary:

- Switch to `Hats.Dinosaur_Hat`.
- Apples spawn.
- Eating apples extends the tail.
- Collision with tail is the main failure mode.
- Longer runs generate more bones.

Baseline safe route:

- Use a serpentine route through columns.
- Leave the bottom row open as a return lane.
- Loop back to origin safely.
- This is reliable but not optimal.

Top-tier improvements:

- Adapt pathing toward the next apple when safe.
- Use shortcuts only if the dinosaur can rejoin the Hamiltonian cycle without trapping itself.
- Tune field size: larger fields give huge potential bone yield but take much longer.

Current save implication:

- Dinosaur is not yet unlocked in `save.json`.
- Do not write dinosaur into the main dispatcher as active work yet.
- Prepare the interface, but gate it behind `num_unlocked(Unlocks.Dinosaurs)`.

### 8. Multi-Drone / Megafarm

At endgame, the main performance unlock is decomposition:

- One drone per row/column for regular crops.
- Drones assigned to maze sectors or separate sub-mazes.
- Coordinator drone handles global harvest decisions, reconfiguration, or unlocks.

Good ownership patterns:

- Column ownership: drone starts on column `x` and only moves north/south within it.
- Row ownership: drone starts on row `y` and only moves east/west within it.
- Block ownership: drone works a rectangular subgrid, useful for partitioned mazes or cactus sorting.

Common failure:

- Assuming `max_drones() == get_world_size()` forever.
- At 32x32, one Reddit post notes 32 drones total means 31 spawned helpers plus the original. The main drone must own the last lane or act as coordinator.

## Save-Specific Strategic Direction

This save should progress in this order:

1. Raise power with a real sunflower max-petal loop.
2. Raise gold reserve using the current maze loop, then improve it.
3. Continue auto-unlocking speed, expansion, drone count, cactus tiers, and maze tiers when reserves allow.
4. Add cactus sorting once cactus reserve/unlock costs become a bottleneck.
5. Refactor code to never assume 9x9.
6. Use `set_world_size()` only for testing, not as the definition of endgame.
7. Add dinosaur/bone module only after `Unlocks.Dinosaurs` appears.
8. Add leaderboard/simulation harness only after the main automation is stable.

## Architecture Recommendations

Recommended modules:

- `main.py`: dispatcher only.
- `farming.py`: shared resource thresholds, till/water/harvest/trade helpers.
- `movement.py`: wrapping movement, lane movement, block movement.
- `poly.py`: base resource recovery.
- `sunflower.py`: max-petal power farming.
- `pumpkin.py`: mega-pumpkin farm with repair loop.
- `cactus.py`: cactus plant/sort/harvest.
- `maze.py`: simple solver now, later multi-drone/pathfinding/reuse.
- `dinosaur.py`: gated bone farming.
- `unlocking.py`: safe unlock checks based on `get_cost()`.
- `benchmark.py`: `simulate()` and `get_tick_count()` helpers.

Dispatcher should choose based on goals, not current method state:

```python
while True:
    if need_power():
        sunflower.run()
    elif need_gold():
        maze.run()
    elif need_base_materials():
        poly.run()
    elif need_unlock_resource():
        run_bottleneck_loop()
    elif can_safely_unlock():
        unlock_next()
    elif cactus_ready_goal():
        cactus.run()
    elif dinosaur_ready_goal():
        dinosaur.run()
    else:
        benchmark_or_farm_next_goal()
```

## Research Conclusions

- Endgame is best modeled as 32x32 and 32-drone-capable, not 9x9.
- The current save is on the path but still needs max expansion/drone/speed and dinosaur/leaderboard unlocks.
- The highest-impact immediate code upgrade is a real dispatcher plus sunflower max-petal farming.
- The highest-impact next specialist loop is cactus sorting.
- Maze should evolve from simple wall-following to measured/pathfinding/reuse and possibly multi-drone or partitioned maze farming.
- Dinosaur should be implemented as a safe Hamiltonian-cycle baseline first, then optimized with apple-aware shortcuts.
- Top-tier play is algorithm selection plus tick/movement minimization, not just planting bigger fields.

## Sources

- Local game definitions: `__builtins__.py` in this save folder.
- Current save state: `save.json` in this save folder.
- Wiki/function references:
  - https://thefarmerwasreplaced.wiki.gg/wiki/Available_Functions
  - https://thefarmerwasreplaced.wiki.gg/wiki/Entities
  - https://thefarmerwasreplaced.wiki.gg/wiki/Cactus
  - https://thefarmerwasreplaced.wiki.gg/wiki/Dinosaurs
  - https://thefarmerwasreplaced.wiki.gg/wiki/Sunflowers
  - https://thefarmerwasreplaced.wiki.gg/wiki/Mazes
  - https://thefarmerwasreplaced.wiki.gg/wiki/Leaderboard
- Strategy/code collections:
  - https://github.com/Flekay/The-Farmer-Was-Replaced
  - https://github.com/eyyMinda/FarmerReplaced
  - https://github.com/Thorrdu/the-farmer-was-replaced
  - https://github.com/Cliencer/The-Farmer-Was-Replaced-Auto
- Cactus sorting:
  - https://thefarmerwasreplaced.com/codes/cactus-code/
  - https://www.reddit.com/r/TheFarmerWasReplaced/comments/1rzxw39/my_leaderboard_cactus_farm_380/
  - https://www.youtube.com/watch?v=LtJNyhQUkH4
- Maze and dinosaur:
  - https://medium.com/%40hanxuyang0826/solving-maze-and-dinosaur-in-the-farmer-was-replaced-17ce201f19cc
  - https://steamcommunity.com/app/2060160/discussions/0/662719183492254069/
  - https://www.reddit.com/r/TheFarmerWasReplaced/comments/1ob8jzc/heres_my_maze_solver_32x32_maze_32_drones_doing_a/
  - https://gist.github.com/1337dondongo/6cb2506bb1847d1b4490260673aa49c4
  - https://steamcommunity.com/app/2060160/discussions/0/786567268147618621/
- Multi-drone / 32x32:
  - https://medium.com/%40hanxuyang0826/use-more-drones-in-the-farmer-was-replaced-217bfeef53cd
  - https://www.reddit.com/r/TheFarmerWasReplaced/comments/1o5i72h/how_to_downgrade_size_of_the_farm/
- Achievement/endgame context:
  - https://www.thegamer.com/the-farmer-was-replaced-achievement-guide/
