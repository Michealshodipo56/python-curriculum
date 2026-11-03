# Totals Along the Way

## Description
A prefix includes every value from the beginning of a sequence through a chosen position. Produce the running total at each position.

## Requirements
- Implement `prefix_sums(nums)` in `starter/solution.py`.
- Return a new list containing one sum for every prefix of `nums`.
- Include negative values in the totals.
- Return `[]` when the input list is empty.
- Preserve the input list.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- How does the next total relate to the previous total?
- What should the output length be?

## Example Behavior
`prefix_sums([2, -1, 4])` → `[2, 1, 5]`; `prefix_sums([])` → `[]`.
