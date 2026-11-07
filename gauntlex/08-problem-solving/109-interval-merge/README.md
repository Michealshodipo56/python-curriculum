# Unify Time Ranges

## Description

Intervals may overlap or share an endpoint. Combine them into the smallest sorted collection of disjoint closed intervals.

## Requirements

- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Each input interval is `[start, end]` with integer endpoints and `start <= end`.
- Merge intervals that overlap or touch at an endpoint.
- Return the resulting intervals sorted by starting point.
- Return `[]` for empty input and do not mutate caller-owned intervals.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- What changes after intervals are ordered by their starts?
- Why should `[1, 3]` and `[3, 5]` combine?

## Example Behavior

`merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]])` → `[[1, 6], [8, 12]]`.
