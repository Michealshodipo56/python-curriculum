# slow_tests

## Challenge
Given a list of [name,duration_seconds] pairs and a nonnegative threshold, return test names whose duration strictly exceeds threshold, ordered by descending duration and then ascending name.

## Requirements
- Implement `slow_tests(records, threshold)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Use a two-part sort key for deterministic ties.

## Run tests
`python -m pytest tests -q`
