# binary_search

## Description
Return the index of an integer target in a sorted list, or -1 if absent. Any matching index is acceptable for duplicates.

## Requirements
- Implement `binary_search(items, target)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`binary_search([1, 3, 5, 7], 5)` → `2`

`binary_search([1, 3, 5], 2)` → `-1`

## Tips
Compare the middle element and discard the half that cannot contain the target.
