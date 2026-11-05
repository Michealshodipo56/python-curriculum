# Unequal Importance

## Description
A weighted mean lets some observations contribute more than others. Each observation has a corresponding nonnegative weight.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Assume numeric `values` and `weights` have equal length and every weight is nonnegative.
- Return the weighted average, with each observation contributing in proportion to its weight.
- Return `None` if the total weight is zero.
- Do not mutate either list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why is a simple arithmetic mean insufficient when weights differ?
- What does a zero weight contribute?

## Example Behavior
`weighted_mean([10, 20], [1, 3])` → `17.5`

`weighted_mean([1, 2], [0, 0])` → `None`
