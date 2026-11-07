# Merge Integer Ranges

## Description
Combine a collection of inclusive integer ranges into a canonical, sorted set of nonoverlapping ranges. Adjacent integer ranges must be combined as well as overlapping ones.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Each input interval is `[start, end]` with `start <= end`; inputs need not be sorted.
- Return merged intervals sorted by their starting value.
- Merge when the next start is at most the current end plus one, because endpoints are inclusive integers.
- Do not mutate input intervals or print.
- Use Python's standard library only.

## Design Considerations
Sort by interval start before combining overlaps, and preserve the intended treatment of touching endpoints. Keep the output ordered and avoid modifying caller-owned intervals.

## Tips
- Why is sorting useful before merging?
- Why do `[1, 2]` and `[3, 4]` merge under this contract?

## Example Behavior
`merge_intervals([[5, 7], [1, 2], [3, 4]])` → `[[1, 7]]`.
