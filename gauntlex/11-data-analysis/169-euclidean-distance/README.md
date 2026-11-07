# Distance in Many Dimensions

## Description
Generalize the familiar straight-line distance between two points to vectors of any matching dimension.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Assume two equal-length numeric vectors.
- Return the square root of the sum of squared coordinate differences.
- Return `0` for two empty vectors.
- Do not modify either input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How does two-dimensional distance extend to more coordinates?
- Why does changing the order of the vectors not change the distance?

## Example Behavior
`euclidean_distance([0, 0], [3, 4])` → `5`

`euclidean_distance([], [])` → `0`
