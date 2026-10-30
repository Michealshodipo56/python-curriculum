# redact_headers

## Challenge
Given a mapping of HTTP header names to strings, return a new mapping with values replaced by `[REDACTED]` for Authorization, Cookie, Set-Cookie and X-API-Key, case-insensitively. Preserve original key casing and other values.

## Requirements
- Implement `redact_headers(headers)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Normalize names only for comparison, not for output.

## Run tests
`python -m pytest tests -q`
