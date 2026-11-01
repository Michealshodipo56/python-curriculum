# Zeros to the Back

## Description
Rearrange a sequence so every zero appears after all nonzero values, without changing the relative order of nonzero elements.

## Requirements
- Implement `move_zeros(items)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`move_zeros([0, 1, 0, 3, 12])` → `[1, 3, 12, 0, 0]`

`move_zeros([0, 0])` → `[0, 0]`

## Tips
Think about constructing a new list instead of changing the caller's collection.

The examples illustrate expected behavior, not an implementation.
