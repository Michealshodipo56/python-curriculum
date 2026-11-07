# Walk the Spiral

## Description

Read a rectangular grid in clockwise spiral order, starting at the top-left corner and moving inward as the outer boundary is exhausted.

## Requirements

- Implement `spiral_order(matrix)` in `starter/solution.py`.
- Assume `matrix` is rectangular.
- Return a flat list of values visited clockwise, starting across the top row.
- Visit every cell exactly once.
- Return `[]` for an empty grid; do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- How do the unvisited boundaries change after completing each side?
- What if only one row or column remains?

## Example Behavior

`spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` → `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.
