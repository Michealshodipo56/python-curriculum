# Quarter Turn

## Description
Rotate a square grid clockwise into a new grid while keeping the original unchanged.

### Behavior contract
Return a new square matrix rotated 90 degrees clockwise. An empty matrix stays empty.

## Requirements
- Implement `rotate_matrix(matrix)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`rotate_matrix([[1, 2], [3, 4]])` → `[[3, 1], [4, 2]]`

`rotate_matrix([])` → `[]`

## Tips
Draw where each corner moves after one clockwise quarter-turn.

The examples define expected behavior; design your own implementation.
