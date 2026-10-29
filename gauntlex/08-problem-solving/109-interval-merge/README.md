# merge_intervals

## Description
Merge overlapping or touching closed integer intervals and return sorted disjoint intervals. Each input interval is [start,end] with start<=end.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]])` → `[[1, 6], [8, 12]]`

`merge_intervals([])` → `[]`

## Tips
Sort by start position and extend the current interval when ranges overlap.
