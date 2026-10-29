# merge_sorted

## Description
Merge two already sorted integer lists into one sorted list, preserving duplicates.

## Requirements
- Implement `merge_sorted(left, right)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`merge_sorted([1, 3, 5], [2, 4])` → `[1, 2, 3, 4, 5]`

`merge_sorted([], [-1, 2])` → `[-1, 2]`

## Tips
Use two positions to select the smaller next item.
