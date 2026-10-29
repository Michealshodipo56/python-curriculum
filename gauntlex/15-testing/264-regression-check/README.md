# regressions

## Challenge
Given mappings test_name->bool for baseline and current runs, return sorted names that passed previously but fail now. Ignore tests absent from either run.

## Requirements
- Implement `regressions(baseline, current)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
A regression is a transition from success to failure.

## Run tests
`python -m pytest tests -q`
