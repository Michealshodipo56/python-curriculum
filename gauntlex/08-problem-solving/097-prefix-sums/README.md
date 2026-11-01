# Totals Along the Way

## Description
Produce a running total after every element of a numeric sequence.

### Behavior contract
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
A prefix includes everything from the beginning through the current position.

The examples define expected behavior; design your own implementation.
