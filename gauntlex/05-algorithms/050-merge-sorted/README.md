# Two Ordered Streams

## Description
Two input lists are already sorted. Combine them into one sorted sequence without losing any values or duplicates.

## Requirements
- Implement `merge_sorted(left, right)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`merge_sorted([1, 3, 5], [2, 4])` → `[1, 2, 3, 4, 5]`

`merge_sorted([], [-1, 2])` → `[-1, 2]`

## Tips
At each step, only the next unconsumed element of each input can be the smallest remaining candidate.

The examples illustrate the contract without providing an implementation.
