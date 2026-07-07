---
title: Current Strategy Index
type: strategy-index
status: active
updated: 2026-07-08
---

# Current Strategy Index

This index links to the live strategy notes for the current codebase. Read this before editing strategy modules, then open the specific strategy file you need.

## Core Strategy Files

- [Dispatcher and shared helpers](dispatcher)
- [Sunflower / power](sunflower)
- [Polyculture / base resources](polyculture)
- [Pumpkin](pumpkin)
- [Cactus](cactus)
- [Maze / gold](maze)
- [Dinosaur / bones](dinosaur)

## Supporting Design Docs

- [Research](../research.md)
- [Benchmarking](../benchmarking.md)

## Current Dispatcher Order

The live dispatcher in `main.py` evaluates jobs in this order:

1. [Sunflower](sunflower) for power.
2. [Polyculture](polyculture) for hay, wood, and carrot.
3. [Pumpkin](pumpkin) for pumpkins.
4. [Cactus](cactus) for cactus.
5. [Dinosaur](dinosaur) for bones.
6. [Maze](maze) for gold.

If no item is below its low target, the fallback is [Maze](maze).

## Current Remaining Strategy Work

- Benchmark the 8-neighbor waiting loop in [Polyculture](polyculture).
- Add benchmarking helpers only when comparing strategies, not in the main loop.
