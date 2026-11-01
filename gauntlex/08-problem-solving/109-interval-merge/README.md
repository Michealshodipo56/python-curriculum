# Unify Time Ranges

## Description
Combine overlapping or touching intervals into a sorted list of separate ranges.

### Behavior contract
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
Once ranges are ordered by start, compare each new range with the current merged range.

The examples define expected behavior; design your own implementation.
