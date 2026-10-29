# move_zeros

## Description
Return a new list with all numeric zeros moved to the end while preserving order of other integers.

## Requirements
- Implement `move_zeros(items)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`move_zeros([0, 1, 0, 3, 12])` → `[1, 3, 12, 0, 0]`

`move_zeros([0, 0])` → `[0, 0]`

## Tips
Separate nonzero items and count zeros before constructing the result.
