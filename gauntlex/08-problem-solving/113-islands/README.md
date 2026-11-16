# Count the Islands

## Description

Implement `count_islands(grid)` in `starter/solution.py`. Count distinct four-directionally connected land regions.

## Requirements

- Implement `count_islands(grid)` in `starter/solution.py`.
- Assume a rectangular grid of `'0'` and `'1'` strings.
- Count distinct four-directionally connected land regions.
- Do not connect cells diagonally.
- Return `0` for an empty grid and do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- **Concept to understand:** A land region is a group of `'1'` cells connected horizontally or vertically. Count the number of separate regions in a grid.
- How can one discovered region be counted only once?
- Why do diagonal neighbors remain separate islands?

## Example Behavior

`count_islands([['1', '1', '0'], ['0', '1', '0'], ['0', '0', '1']])` → `2`; `count_islands([])` → `0`.
