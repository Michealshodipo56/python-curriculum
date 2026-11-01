# Distance in Many Dimensions

## Description
Compute the straight-line distance between two numeric vectors.

### Behavior contract
Return Euclidean distance between two equal-length numeric vectors. Empty vectors have distance zero.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`euclidean_distance([0, 0], [3, 4])` → `5`

`euclidean_distance([], [])` → `0`

## Tips
Think about how the familiar two-dimensional distance formula generalizes.

Examples illustrate expected values, not a solution.
