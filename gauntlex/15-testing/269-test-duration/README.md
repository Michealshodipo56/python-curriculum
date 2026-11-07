# Find Slow Cases

## Description

Performance reports can prioritize slow tests. Select only tests exceeding a threshold and rank them predictably.

## Requirements

- Implement `slow_tests(records, threshold)` in `starter/solution.py`.
- Accept `[name, duration_seconds]` pairs and a nonnegative threshold.
- Include only names whose duration is strictly greater than the threshold.
- Sort qualifying tests by duration descending, then name ascending.
- Return the names only.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why does a duration equal to the threshold not qualify?

## Example Behavior

`slow_tests([['a', 2], ['b', 3], ['c', 3]], 2)` → `['b', 'c']`.
