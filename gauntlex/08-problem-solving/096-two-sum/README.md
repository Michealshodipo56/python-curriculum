# two_sum

## Description
Return indices [i,j] of two different elements summing to target, with i<j. If multiple pairs exist, choose the pair with smallest j, then smallest i. Return [] if none.

## Requirements
- Implement `two_sum(nums, target)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`two_sum([2, 7, 11, 15], 9)` → `[0, 1]`

`two_sum([3, 3], 6)` → `[0, 1]`

## Tips
Track previously seen values and their earliest indices.
