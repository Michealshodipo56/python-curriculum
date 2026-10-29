# rate_limit_allowed

## Challenge
Given sorted integer request timestamps, current integer time, positive window, and nonnegative limit, return True if fewer than limit requests occurred in the half-open interval (now-window,now].

## Requirements
- Implement `rate_limit_allowed(timestamps, now, window, limit)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Carefully implement the open lower boundary.

## Run tests
`python -m pytest tests -q`
