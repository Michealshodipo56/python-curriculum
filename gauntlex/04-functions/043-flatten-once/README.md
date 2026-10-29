# flattenonce

## Description
Implement `flatten_once(groups)` returning a new list of the elements from each inner list in order. Assume a list of lists.

## Requirements
- Implement the named function in `solution.py`.
- Return the value; do not print it.
- Do not add executable input handling at module import time.

## Examples
`flattenonce([[1, 2], [3], []])` → `[1, 2, 3]`

`flattenonce([[], [4]])` → `[4]`

## Tips
Nested iteration lets you visit each group and each member. Do not modify the input.
