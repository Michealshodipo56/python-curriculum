# pascal_row

## Description
Return row n of Pascal's triangle as a list of integers. Row 0 is [1]; assume n is nonnegative.

## Requirements
- Implement `pascal_row(n)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`pascal_row(0)` → `[1]`

`pascal_row(1)` → `[1, 1]`

## Tips
Each interior value is the sum of two adjacent values in the preceding row.
