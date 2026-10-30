# random_token

## Challenge
Return a URL-safe Base64 token representing exactly n cryptographically random bytes, without trailing padding. Require n>=1. Tests check format and decoded length, not a fixed random output.

## Requirements
- Implement `random_token(n)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Use secrets.token_bytes, not random.Random.

## Run tests
`python -m pytest tests -q`
