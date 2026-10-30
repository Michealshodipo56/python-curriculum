# shortest_path_grid

## Challenge
Given a rectangular grid of 0 (open) and 1 (blocked), return minimum number of four-direction moves from top-left to bottom-right, or -1 if unreachable. Return -1 for empty grid or blocked endpoints. Assume rows have equal length.

## Requirements
- Implement `shortest_path_grid(grid)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Breadth-first search discovers shortest paths in an unweighted grid.

## Run tests
`python -m pytest tests -q`
