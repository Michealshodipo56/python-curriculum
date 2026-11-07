# Matrix Composition

## Description
Matrix multiplication combines rows from one matrix with columns from another. The resulting grid has dimensions determined by the outer dimensions of the inputs.

## Requirements
- Implement `matrix_multiply(a, b)` in `starter/solution.py`.
- Assume `a` and `b` are nonempty, rectangular, numeric matrices with compatible dimensions.
- Return a new matrix representing the product `a * b`.
- Each output entry combines one row of `a` with one column of `b`.
- Do not modify either input matrix.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must the number of columns in the first matrix match the number of rows in the second?
- How is multiplication different from elementwise addition?

## Example Behavior
`matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[19, 22], [43, 50]]`

`matrix_multiply([[2]], [[3]])` → `[[6]]`
