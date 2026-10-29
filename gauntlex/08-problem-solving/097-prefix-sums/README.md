# prefix_sums

## Description
Return running totals for the integer list, with one total for each prefix.

## Requirements
- Implement `prefix_sums(nums)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`prefix_sums([2, -1, 4])` → `[2, 1, 5]`

`prefix_sums([])` → `[]`

## Tips
A single accumulator can record the total after each item.
