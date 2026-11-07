# Best Continuous Segment

## Description

A contiguous subarray is an uninterrupted stretch of a list. Find the largest possible sum of a nonempty stretch, even when every number is negative.

## Requirements

- Implement `max_subarray(nums)` in `starter/solution.py`.
- Assume `nums` is a nonempty list of integers.
- Return the maximum sum among all nonempty contiguous subarrays.
- Do not treat an empty subarray as a candidate.
- Do not modify `nums`.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Why can the best answer be negative?
- When can extending a segment make its sum worse?

## Example Behavior

`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` → `6`; `max_subarray([-4, -2, -8])` → `-2`.
