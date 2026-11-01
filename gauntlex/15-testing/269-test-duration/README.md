# Find Slow Cases

## Description
Rank tests whose runtimes exceed a threshold, using stable tie-breaking.

### Behavior contract
Given a list of [name,duration_seconds] pairs and a nonnegative threshold, return test names whose duration strictly exceeds threshold, ordered by descending duration and then ascending name.

## Requirements
- Implement `slow_tests(records, threshold)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
The threshold is strict: a duration equal to it does not qualify.

Work from the contract and edge cases; do not include a finished implementation.
