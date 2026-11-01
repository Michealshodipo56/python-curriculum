# Smallest Sufficient Window

## Description
Find the shortest consecutive group of positive integers whose sum reaches a target.

### Behavior contract
Return the minimum length of a contiguous subarray with sum at least target, or 0 if none exists. All nums are positive integers and target is positive.

## Requirements
- Implement `min_subarray_len(target, nums)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`min_subarray_len(7, [2, 3, 1, 2, 4, 3])` → `2`

`min_subarray_len(15, [1, 2, 3, 4, 5])` → `5`

## Tips
Positive values make it possible to adjust the ends of a window predictably.

The examples define expected behavior; design your own implementation.
