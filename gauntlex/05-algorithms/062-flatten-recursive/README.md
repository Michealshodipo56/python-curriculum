# flatten_recursive

## Description
Flatten a nested list of integers to one list in left-to-right order. Nesting may be arbitrarily deep.

## Requirements
- Implement `flatten_recursive(items)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`flatten_recursive([1, [2, [3]], 4])` → `[1, 2, 3, 4]`

`flatten_recursive([])` → `[]`

## Tips
A recursive function can process a nested list by applying the same rule to each child list.
