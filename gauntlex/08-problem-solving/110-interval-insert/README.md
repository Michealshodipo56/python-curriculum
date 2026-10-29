# insert_interval

## Description
Given sorted nonoverlapping closed intervals and one new interval, insert and merge overlapping or touching intervals.

## Requirements
- Implement `insert_interval(intervals, new_interval)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`insert_interval([[1, 3], [6, 9]], [2, 5])` → `[[1, 5], [6, 9]]`

`insert_interval([], [2, 4])` → `[[2, 4]]`

## Tips
Handle intervals before, overlapping, and after the new interval.
