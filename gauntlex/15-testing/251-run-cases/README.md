# run_cases

## Challenge
Given a callable fn and list of [args,expected] cases where args is a list, return a list of booleans indicating whether fn(*args) equals expected. Let exceptions propagate.

## Requirements
- Implement `run_cases(fn, cases)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Keep each case independent and preserve its position.

## Run tests
`python -m pytest tests -q`
