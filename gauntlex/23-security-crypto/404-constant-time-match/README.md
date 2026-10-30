# constant_time_match

## Challenge
Given two UTF-8 strings, return whether they are equal using a constant-time comparison primitive from the standard library. Do not implement a manual early-exit loop.

## Requirements
- Implement `constant_time_match(a, b)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Compare encoded byte strings using hmac.compare_digest.

## Run tests
`python -m pytest tests -q`
