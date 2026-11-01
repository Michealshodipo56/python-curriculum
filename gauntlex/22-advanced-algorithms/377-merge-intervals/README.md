# Merge Integer Ranges

## Description
Combine overlapping or adjacent integer intervals into disjoint sorted ranges.

### Behavior contract
Given a list of inclusive integer intervals [start,end] with start<=end, return merged intervals sorted by start. Overlapping or touching intervals (next.start<=current.end+1) merge. Do not mutate inputs.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
For inclusive integer intervals, touching can include consecutive endpoints.

The task is to design an implementation that meets both behavior and efficiency requirements.
