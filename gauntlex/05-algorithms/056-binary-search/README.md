# Halve the Search

## Description
Locate a value in an already sorted list by repeatedly narrowing the region where it could occur.

## Requirements
- Implement `binary_search(items, target)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`binary_search([1, 3, 5, 7], 5)` → `2`

`binary_search([1, 3, 5], 2)` → `-1`

## Tips
Each comparison should rule out an entire portion of the remaining search interval.

The examples illustrate expected behavior, not an implementation.
