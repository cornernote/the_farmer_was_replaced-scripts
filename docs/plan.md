---
title: Optimized Endgame Strategy Plan
type: plan
status: active
source: docs/research.md
updated: 2026-07-04
---

# Optimized Endgame Strategy Plan

Research source: `docs/research.md`

This save is late-midgame, not endgame. It currently has `expand_9`, polyculture, pumpkins, sunflowers/power, cactus, mazes/gold, simulation, multi-drone support, `set_world_size`, and wizard hat. True endgame strategy should target 32x32-safe, 32-drone-capable automation.

The goal is to build a resilient progression dispatcher that can:

- keep core resources stable
- farm bottlenecks for the next unlock
- safely unlock toward max expansion/drone/speed tiers
- run specialist algorithms for power, gold, pumpkins, cactus, and later bones
- benchmark and improve loops without hard-coding the current 9x9 state

## Guiding Rules

1. Never assume 9x9 is the destination.
   Use `get_world_size()` and `max_drones()` in production loops. Use fixed sizes only in small test/benchmark scripts.

2. Treat endgame as algorithms, not bigger crop loops.
   Sunflowers need max-petal selection, pumpkins need synchronization, cactus needs sorting, mazes need pathfinding/reuse, and dinosaurs need safe path planning.

3. Keep the dispatcher simple and conservative.
   It should choose one job based on shortages, unlock costs, and gated mechanics. Specialist modules should not also make global unlock decisions.

4. Use lane/block ownership for drones.
   Spawned drones should own rows, columns, or blocks. The main drone either owns the remaining lane or coordinates global decisions.

5. Build baseline correctness before leaderboard optimization.
   A correct bubble/cocktail cactus sort beats an incomplete clever sorter. A reliable wall-following maze beats a broken pathfinder.

## Current Code Assessment

Existing files:

- `main.py`: simple dispatcher for maze, polyculture, and pumpkins.
- `farming.py`: shared till/water/harvest and resource checks.
- `movement.py`: wrapped movement and maze helpers.
- `poly.py`: companion-based mixed farming with row drones.
- `pumpkin.py`: multi-pass pumpkin loop with fertilizer use.
- `maze.py`: left-hand wall-following maze solver.

Keep this modular shape, but change the plan from "three loops" to a gated progression system.

## Target Module Layout

Required near-term modules:

- `sunflower.py`: max-petal power farming.
- `unlocking.py`: safe unlock checks using `get_cost()` and reserves.
- `cactus.py`: cactus plant/sort/harvest.
- `benchmark.py`: optional `get_tick_count()` and `simulate()` helpers.

Later modules:

- `dinosaur.py`: gated behind `num_unlocked(Unlocks.Dinosaurs)`.
- advanced `maze.py` modes: mapped pathfinding, reuse, multi-drone or partitioned mazes.

## Resource Policy

Use named reserves in `farming.py`. These are progression reserves, not final leaderboard values.

| Resource | Current Purpose | Minimum | Preferred |
| --- | --- | ---: | ---: |
| Hay | base unlocks/trades | 2,000,000 | 10,000,000 |
| Wood | base unlocks/trades | 2,000,000 | 10,000,000 |
| Carrot | base unlocks/trades | 1,000,000 | 5,000,000 |
| Pumpkin | unlocks and burst income | 1,000,000 | 5,000,000 |
| Water | soil loop support | 25,000 | 100,000 |
| Fertilizer | pumpkins, weird substance, burst loops | 100 | 1,000 |
| Weird Substance | mazes/gold | 100,000 | 500,000 |
| Power | speed/progression support | 5,000 | 25,000 |
| Gold | unlock bottleneck | 1,000 | 10,000 |
| Cactus | cactus unlock path | 10,000 | 100,000 |
| Bone | post-dinosaur unlock path | 10,000 | 100,000 |

Adjust upward as unlock costs increase. The dispatcher should prefer farming the next known bottleneck over blindly filling every preferred reserve.

## Dispatcher Policy

The dispatcher should evaluate jobs in this order:

1. If power is below minimum and sunflowers are unlocked: run `sunflower`.
2. If gold is below minimum and mazes are unlocked: run `maze`.
3. If base materials are below minimum: run `poly`.
4. If a safe unlock is available without dropping below reserves: unlock it.
5. If the next unlock has a known bottleneck: farm that bottleneck.
6. If pumpkin stock is below preferred: run `pumpkin`.
7. If cactus is unlocked and cactus stock is below target: run `cactus`.
8. If dinosaurs are unlocked and bones are below target: run `dinosaur`.
9. Otherwise benchmark or farm the next predicted bottleneck.

Target shape:

```python
def run_once():
    job = select_job()
    job["run"]()

while True:
    run_once()
```

Job records should include:

- `name`
- `enabled`
- `need`
- `run`
- `requires`
- `reserve_items`

Do not build `world` state globally in `main.py`; let each module initialize only when selected.

## Phase 1: Stabilize And Refactor

Purpose: make the current bot safe to extend.

Tasks:

- Move thresholds into `farming.py`.
- Add `has_unlock(unlock)` wrappers around `num_unlocked()`.
- Add `can_afford_without_reserve(cost)` in a new `unlocking.py`.
- Replace chained `if/elif` in `main.py` with job selection.
- Keep current `poly`, `pumpkin`, and `maze` behavior while the dispatcher changes.
- Remove any plan/code comments that imply 9x9 is endgame.

Acceptance:

- Existing loops still run.
- Dispatcher chooses power/gold/base/pumpkin by explicit job rules.
- New mechanics are gated before use.

## Phase 2: Real Sunflower Power

Purpose: fix the current weak power strategy.

Current issue:

- `poly.py` plants sunflowers when power is low, but it does not measure petals or harvest the max-petal sunflower.

Implement `sunflower.py`:

1. Fill a field or owned lanes with sunflowers.
2. Wait/loop until enough are harvestable.
3. Measure petals with `measure()`.
4. Track max-petal positions.
5. Harvest only max-petal flowers while the bonus condition is satisfied.
6. Replant harvested tiles.
7. Exit once power reaches target.

Optimization path:

- Baseline: single-drone full-field scan.
- Next: lane drones plant/maintain, coordinator harvests max-petal candidates.
- Benchmark: power per tick.

Acceptance:

- Power target rises materially faster than the current polyculture fallback.
- No fixed-size assumptions.

## Phase 3: Safer Gold And Maze Growth

Purpose: gold is the current progression bottleneck.

Keep baseline:

- Current wall-following solver is valid for loop-free mazes.
- Raise gold reserve from the old `100` threshold.

Immediate improvements:

- Guard maze creation with enough weird substance.
- If weird substance is short, run polyculture or a focused fertilizer/tree support loop.
- Use the correct substance formula from current code: `get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)`.
- Add simple timing around maze runs.

Later improvements:

- Use `measure()` to locate treasure.
- Record maze connectivity and pathfind to treasure.
- Add maze reuse mode for achievements/progression where valid.
- Test multi-drone search and partitioned 8x8 maze blocks once the farm approaches 32x32.

Acceptance:

- Maze loop never burns the last weird substance reserve.
- Gold reserve supports unlock progression.

## Phase 4: Unlock Management

Purpose: stop progression from being manual.

Implement `unlocking.py`:

```python
def cost_of(unlock):
    return get_cost(unlock)

def can_unlock_safely(unlock):
    cost = cost_of(unlock)
    if cost == None:
        return False
    return can_afford_without_reserve(cost)
```

Priority order:

1. Speed/execution upgrades.
2. Expansion toward 32x32.
3. Drone count/megafarm.
4. Sunflower/power support if not maxed.
5. Maze/gold support.
6. Cactus tiers.
7. Dinosaur/bone unlocks.
8. Leaderboards and final/cosmetic unlocks.

After any expansion/drone unlock:

- Recompute world size.
- Rebuild any cached worlds.
- Prefer dynamic loops over fixed path lists.

Acceptance:

- Unlock attempts never drop resources below minimum reserves.
- Dispatcher can farm the next bottleneck when an unlock is not affordable.

## Phase 5: Pumpkin Upgrade

Purpose: turn the existing pumpkin loop into a scalable mega-pumpkin loop.

Baseline changes:

- Keep dead-pumpkin repair.
- Keep full-field harvest delayed until the field is mature.
- Preserve fertilizer reserve for weird substance and cactus work.

32x32-safe upgrade:

- Assign drones by column or row.
- Each worker maintains its lane.
- Main drone checks representative tiles/corners with `measure()` or maturity checks.
- Harvest only when the full connected mega pumpkin is ready.

Acceptance:

- No fixed pass count that assumes current farm size.
- Dead pumpkins are repaired before final harvest.

## Phase 6: Cactus Sorting

Purpose: cactus is the next major specialist algorithm already unlocked.

Mechanic:

- Cactus sizes must be sorted so adjacent sorted cacti recursively harvest.
- Reward scales with harvested group size squared.

Baseline implementation:

1. Plant cactus across the field.
2. Wait until all target tiles are cactus and harvestable.
3. Sort using neighbor `measure(direction)` and `swap(direction)`.
4. Harvest after no swaps are needed.

Recommended first algorithm:

- Cocktail shaker style over rows and columns.
- Shrink active bounds as edges settle.
- Keep it readable and correct before optimizing.

Later optimization:

- Insertion-style placement.
- Block-level sorting for large fields.
- Movement minimization and cached position planning.

Acceptance:

- Works at current size.
- Uses `get_world_size()`.
- Can be benchmarked against cactus per tick.

## Phase 7: Megafarm Scaling

Purpose: prepare for true 32x32.

Patterns to use:

- Row ownership for row-major crop passes.
- Column ownership for pumpkins/sunflowers/base loops.
- Block ownership for maze partitions and maybe cactus experiments.
- Main drone handles leftover lane or coordinator duties.

Avoid:

- Assuming spawned drones equal world size.
- Spawning workers that wander globally.
- Shared mutable world updates without clear ownership.

Acceptance:

- Each multi-drone loop has a clear ownership model.
- Main drone still does useful work when only `max_drones() - 1` helpers can be spawned.

## Phase 8: Dinosaur / Bones

Purpose: implement only after the unlock appears.

Gate:

```python
num_unlocked(Unlocks.Dinosaurs) > 0
```

Baseline:

- Switch to `Hats.Dinosaur_Hat`.
- Follow a Hamiltonian/serpentine path.
- Leave a return lane open.
- Avoid self-collision over chasing apples aggressively.

Optimization:

- Add apple-aware shortcuts only when the path can safely rejoin the cycle.
- Benchmark field size versus bones per tick.

Acceptance:

- Dinosaur module is inert until unlocked.
- First implementation prioritizes safety over clever shortcuts.

## Phase 9: Benchmarking And Leaderboards

Purpose: move from progression automation to top-tier strategy.

Add `benchmark.py` helpers:

- `start = get_tick_count()`
- run one loop
- compare item delta
- print resource per tick

Use `simulate()` for risky changes and `leaderboard_run()` only after leaderboards are unlocked.

Benchmark order:

1. Sunflower power per tick.
2. Maze gold per tick.
3. Pumpkin yield per tick.
4. Cactus per tick.
5. Polyculture base resources per tick.
6. Dinosaur bones per tick after unlock.

## Implementation Checklist

- [ ] Move thresholds and reserves into `farming.py`.
- [ ] Add unlock guards and safe cost checks in `unlocking.py`.
- [ ] Refactor `main.py` to a job selector.
- [ ] Add `sunflower.py` with max-petal harvesting.
- [ ] Raise and protect gold/weird-substance reserves.
- [ ] Add simple benchmark timing around maze and sunflower loops.
- [ ] Upgrade pumpkin loop to use dynamic maturity/repair checks.
- [ ] Add `cactus.py` with cocktail-shaker sorting.
- [ ] Make every loop 32x32-safe with `get_world_size()`.
- [ ] Add lane/block drone ownership for scalable loops.
- [ ] Add `dinosaur.py` only after `Unlocks.Dinosaurs`.
- [ ] Add simulation/leaderboard harness after stable progression.

## Near-Term Build Order

The best next coding sequence is:

1. Refactor dispatcher and thresholds.
2. Add sunflower power loop.
3. Add safe unlock helper.
4. Improve maze reserve handling.
5. Add cactus sorting.
6. Upgrade pumpkin for lane ownership.
7. Add advanced maze/pathfinding.
8. Add dinosaur after unlock.

This order matches the current save: power and gold are immediate constraints, cactus is already unlocked, and dinosaur/leaderboards are future-gated.
