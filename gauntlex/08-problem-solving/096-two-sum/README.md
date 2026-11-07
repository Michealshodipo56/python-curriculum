# Find the Pair

## Description
Find two different positions in an integer list whose values add to a target. When several answers exist, the order in which pairs finish determines which answer is chosen.

## Requirements
- Implement `two_sum(nums, target)` in `starter/solution.py`.
- Return a list `[i, j]` of zero-based indices where `i < j` and `nums[i] + nums[j] == target`.
- If multiple pairs exist, choose the smallest `j`, then the smallest `i`.
- Return `[]` when no matching pair exists.
- Never use the same position twice.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does the pair's second index determine which answer comes first?
- Consider repeated values and negative numbers.

## Example Behavior
`two_sum([2, 7, 11, 15], 9)` → `[0, 1]`; `two_sum([3, 3], 6)` → `[0, 1]`.
