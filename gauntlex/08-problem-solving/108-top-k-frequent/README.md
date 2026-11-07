# Most Common Values

## Description

Rank integer values by frequency. If two values appear equally often, the smaller integer comes first.

## Requirements

- Implement `top_k_frequent(nums, k)` in `starter/solution.py`.
- Assume `0 <= k <=` the number of distinct values in `nums`.
- Return exactly `k` distinct integers.
- Order them by descending frequency, then ascending numeric value.
- Return `[]` when `k` is zero.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Why does a frequency ranking need an explicit tie-breaker?
- How should negative values behave when counts tie?

## Example Behavior

`top_k_frequent([1, 1, 1, 2, 2, 3], 2)` → `[1, 2]`; `top_k_frequent([4, 4, 5, 5, 3], 2)` → `[4, 5]`.
