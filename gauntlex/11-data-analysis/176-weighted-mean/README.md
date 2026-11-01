# Unequal Importance

## Description
Compute an average where observations contribute according to assigned nonnegative weights.

### Behavior contract
Return the weighted average of equal-length numeric values and weights. All weights are nonnegative; return None if the sum of weights is zero.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`weighted_mean([10, 20], [1, 3])` → `17.5`

`weighted_mean([1, 2], [0, 0])` → `None`

## Tips
If every weight is zero, there is no meaningful weighted average.

Examples illustrate expected values, not a solution.
