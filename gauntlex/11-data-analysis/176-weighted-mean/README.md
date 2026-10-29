# weighted_mean

## Challenge
Return the weighted average of equal-length numeric values and weights. All weights are nonnegative; return None if the sum of weights is zero.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`weighted_mean([10, 20], [1, 3])` → `17.5`

`weighted_mean([1, 2], [0, 0])` → `None`

## Hints
Divide the sum of weighted values by the total weight.
