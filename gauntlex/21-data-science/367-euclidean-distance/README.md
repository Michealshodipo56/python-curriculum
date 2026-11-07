# Straight-Line Distance

## Description
Numeric vectors represent points in a coordinate space. Measure their straight-line separation across all dimensions.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Require vectors of equal length, or raise `ValueError`.
- Return the square root of the sum of squared coordinate differences.
- Return `0` for two empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why can vectors of different dimensions not be compared directly?

## Example Behavior
`euclidean_distance([0, 0], [3, 4])` → `5.0`.
