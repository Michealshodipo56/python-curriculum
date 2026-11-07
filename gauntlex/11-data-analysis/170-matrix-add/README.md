# Add Two Grids

## Description

Matrix addition combines two grids of identical shape by adding entries at matching positions.

## Requirements

- Implement `matrix_add(a, b)` in `starter/solution.py`.
- Assume two equal-shaped rectangular numeric matrices.
- Return a new matrix whose entries are sums of corresponding input entries.
- Return `[]` when both matrices are empty.
- Preserve the structure and contents of both input matrices.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- Why must the two shapes match?
- What should happen to an empty matrix?

## Example Behavior

`matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[6, 8], [10, 12]]`

`matrix_add([], [])` → `[]`
