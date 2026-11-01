# Add Two Grids

## Description
Add matching elements from two rectangular matrices without modifying either input.

### Behavior contract
Return the elementwise sum of two equal-shaped rectangular numeric matrices. Empty matrices return [].

## Requirements
- Implement `matrix_add(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[6, 8], [10, 12]]`

`matrix_add([], [])` → `[]`

## Tips
Each output position depends on the same position in both inputs.

Examples illustrate expected values, not a solution.
