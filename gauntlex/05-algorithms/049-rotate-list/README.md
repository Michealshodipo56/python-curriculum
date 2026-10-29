# rotate_right

## Description
Return a new list rotated right by k positions. k is nonnegative; an empty list stays empty.

## Requirements
- Implement `rotate_right(items, k)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`rotate_right([1, 2, 3, 4], 1)` → `[4, 1, 2, 3]`

`rotate_right([1, 2], 5)` → `[2, 1]`

## Tips
Modulo reduces rotations larger than the list length.
