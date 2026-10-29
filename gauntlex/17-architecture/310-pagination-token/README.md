# encode_cursor

## Challenge
Given a nonnegative integer offset, return a URL-safe Base64 string without padding encoding its ASCII decimal representation. Raise ValueError for negative offsets.

## Requirements
- Implement `encode_cursor(offset)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Base64 URL-safe encoding supports opaque-looking cursor tokens.

## Run tests
`python -m pytest tests -q`
