# Best Continuous Segment

## Description
Find the largest sum obtainable from one nonempty, uninterrupted segment.

### Behavior contract
Return the maximum sum of a nonempty contiguous subarray. Assume nums is nonempty.

## Requirements
- Implement `max_subarray(nums)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` → `6`

`max_subarray([-4, -2, -8])` → `-2`

## Tips
A segment must remain contiguous, and an all-negative input still needs a result.

The examples define expected behavior; design your own implementation.
