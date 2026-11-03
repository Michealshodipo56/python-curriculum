# Quarter Turn

## Description
A square matrix can be rotated clockwise by a quarter turn. Return the transformed grid without changing the original rows.

## Requirements
- Implement `rotate_matrix(matrix)` in `starter/solution.py`.
- Assume `matrix` is a square list of lists.
- Return a new matrix rotated exactly 90 degrees clockwise.
- Return `[]` for an empty matrix.
- Do not mutate any original row.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Where does each corner move after one clockwise rotation?
- Consider a one-cell grid and an empty grid.

## Example Behavior
`rotate_matrix([[1, 2], [3, 4]])` → `[[3, 1], [4, 2]]`; `rotate_matrix([])` → `[]`.
