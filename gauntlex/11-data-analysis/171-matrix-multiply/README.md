# Matrix Composition

## Description
Multiply two compatible matrices to produce a new matrix.

### Behavior contract
Return matrix product A*B for compatible nonempty rectangular numeric matrices.

## Requirements
- Implement `matrix_multiply(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[19, 22], [43, 50]]`

`matrix_multiply([[2]], [[3]])` → `[[6]]`

## Tips
Each output cell combines one input row with one input column.

Examples illustrate expected values, not a solution.
