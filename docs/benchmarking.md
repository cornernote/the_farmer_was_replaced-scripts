---
title: Benchmarking And Leaderboard Harness
type: guide
status: active
updated: 2026-07-04
source_task: task-12-leaderboard-simulation-harness
---

# Benchmarking And Leaderboard Harness

`benchmark.py` is opt-in tooling. It is not imported by `main.py`, and none of its helpers run automatically.

## Item Delta Benchmark

Use `benchmark.run()` around a single bounded action:

```python
import benchmark
import maze

benchmark.run('maze', maze.walk_maze, [Items.Gold, Items.Weird_Substance])
```

The helper records `get_tick_count()` and item amounts before the action, runs the action once, then prints tick and item deltas.

## Simulation

Use `benchmark.run_simulation()` to call the game `simulate()` builtin:

```python
import benchmark

benchmark.run_simulation(
	'main',
	Unlocks,
	{Items.Hay: 1000, Items.Wood: 1000},
	{},
	1,
	64
)
```

Keep simulations separate from the live progression loop. Use them to compare specialist modules before enabling dispatcher flags.

## Leaderboard

Leaderboard runs are guarded by an explicit confirmation argument:

```python
import benchmark

benchmark.start_leaderboard(Leaderboards.Maze, 'maze_run', 256, True)
```

If `confirm` is `False`, the helper prints a skipped message and does not call `leaderboard_run()`.

Do not call leaderboard helpers from `main.py`.
