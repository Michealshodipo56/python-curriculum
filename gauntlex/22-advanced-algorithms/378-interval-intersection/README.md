# Where Ranges Overlap

## Description
Find every region shared by two ordered interval collections. Each collection already contains disjoint inclusive ranges, so compare their boundaries without combining unrelated regions.

## Requirements
- Implement `interval_intersection(a, b)` in `starter/solution.py`.
- Both inputs are sorted lists of pairwise-disjoint inclusive integer intervals.
- Return all nonempty pairwise intersections as `[start, end]` ranges in ascending order.
- An intersection consisting of one shared endpoint counts.
- Do not mutate either input or print.
- Use Python's standard library only.

## Tips
- Which of two current intervals can no longer overlap later intervals?
- When is the overlap a single point rather than an empty interval?

## Example Behavior
`interval_intersection([[1, 3], [6, 8]], [[3, 6]])` → `[[3, 3], [6, 6]]`.
