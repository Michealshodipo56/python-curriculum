# count_islands

## Description
Return the number of four-directionally connected groups of '1' in a rectangular grid of strings '0' and '1'. Do not mutate the grid.

## Requirements
- Implement `count_islands(grid)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`count_islands([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]])` → `2`

`count_islands([])` → `0`

## Tips
Each unvisited land cell begins a traversal that marks one island.
