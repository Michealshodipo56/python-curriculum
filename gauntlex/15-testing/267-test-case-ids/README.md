# case_ids

## Challenge
Given a list of test case dictionaries with a `name` string, return IDs `name#N` where N is the 1-based occurrence count for that name.

## Requirements
- Implement `case_ids(cases)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Keep separate occurrence counters per name.

## Run tests
`python -m pytest tests -q`
