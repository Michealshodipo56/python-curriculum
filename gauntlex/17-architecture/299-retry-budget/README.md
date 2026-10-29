# retry_budget

## Challenge
Given a nonnegative request count, nonnegative ratio, and nonnegative retries already used, return the maximum of zero and floor(requests*ratio)-retries_used.

## Requirements
- Implement `retry_budget(requests, ratio, retries_used)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
A retry budget prevents uncontrolled retry storms.

## Run tests
`python -m pytest tests -q`
