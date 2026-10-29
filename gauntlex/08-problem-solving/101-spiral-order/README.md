# spiral_order

## Description
Return a list of matrix elements visited clockwise from the top-left in spiral order. Assume a rectangular matrix.

## Requirements
- Implement `spiral_order(matrix)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` → `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

`spiral_order([])` → `[]`

## Tips
Shrink the top, bottom, left, and right boundaries after each side.
