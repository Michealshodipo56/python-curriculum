# Rows Become Columns

## Description

Implement `transpose(matrix)` in `starter/solution.py`. Return a new matrix whose rows correspond to the original columns.

## Requirements

- Implement `transpose(matrix)` in `starter/solution.py`.
- Assume a rectangular list of rows, all of equal length.
- Return a new matrix whose rows correspond to the original columns.
- Return `[]` for an empty matrix or a matrix with zero columns.
- Do not modify input, print, or execute code on import.

## Tips

- **Concept to understand:** Transposing a matrix exchanges its rows and columns. Build a function that returns a new matrix with each element moved to its corresponding transposed position.
- Draw a small rectangular grid and track the row and column of one element.
- How do the dimensions change after transposition?

## Example Behavior

`transpose([[1, 2], [3, 4]])` → `[[1, 3], [2, 4]]`; `transpose([[1, 2, 3]])` → `[[1], [2], [3]]`.
