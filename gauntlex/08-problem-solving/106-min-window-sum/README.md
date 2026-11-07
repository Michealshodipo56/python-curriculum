# Smallest Sufficient Window

## Description
Find the shortest uninterrupted group of positive integers whose sum reaches or exceeds a target.

## Requirements
- Implement `min_subarray_len(target, nums)` in `starter/solution.py`.
- Assume `target` and all elements of `nums` are positive integers.
- Return the minimum length of a contiguous subarray with sum at least `target`.
- Return `0` when no qualifying subarray exists.
- Do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does the positivity of all numbers matter?
- When might shortening a qualifying window preserve its sum threshold?

## Example Behavior
`min_subarray_len(7, [2, 3, 1, 2, 4, 3])` → `2`; `min_subarray_len(15, [1, 2, 3, 4, 5])` → `5`.
