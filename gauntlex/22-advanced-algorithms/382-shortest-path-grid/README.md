# Shortest Grid Route

## Description
Find the minimum number of moves between two grid corners while avoiding blocked cells.

### Behavior contract
Given a rectangular grid of 0 (open) and 1 (blocked), return minimum number of four-direction moves from top-left to bottom-right, or -1 if unreachable. Return -1 for empty grid or blocked endpoints. Assume rows have equal length.

## Requirements
- Implement `shortest_path_grid(grid)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Unweighted shortest paths can be explored in layers.

The task is to design an implementation that meets both behavior and efficiency requirements.
