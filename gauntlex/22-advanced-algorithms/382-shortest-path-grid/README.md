# Shortest Grid Route

## Description
Navigate a rectangular grid from its upper-left corner to its lower-right corner while avoiding blocked cells. Return the fewest orthogonal moves, not the number of visited cells.

## Requirements
- Implement `shortest_path_grid(grid)` in `starter/solution.py`.
- Cells are `0` for open and `1` for blocked; assume equal row lengths.
- Movement is permitted up, down, left, or right, never diagonally.
- Return the minimum number of moves from top-left to bottom-right.
- Return `-1` for an empty grid, blocked endpoint, or unreachable destination.
- Do not mutate the grid or print.
- Use Python's standard library only.

## Tips
- Why does exploring reachable cells by distance layers find a shortest route?
- How many moves does a single open cell require?

## Example Behavior
`shortest_path_grid([[0, 0], [1, 0]])` → `2`; `shortest_path_grid([[1]])` → `-1`.
