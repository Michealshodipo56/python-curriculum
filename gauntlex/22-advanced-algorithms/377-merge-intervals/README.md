# merge_intervals

## Challenge
Given a list of inclusive integer intervals [start,end] with start<=end, return merged intervals sorted by start. Overlapping or touching intervals (next.start<=current.end+1) merge. Do not mutate inputs.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Hint
Sort by start, then extend the most recent merged interval.

## Run tests
`python -m pytest tests -q`
