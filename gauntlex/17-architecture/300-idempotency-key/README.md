# idempotency_key

## Challenge
Given a method, URL, and request body string, return a stable lowercase SHA-256 hex digest of compact JSON encoding of [method.upper(),url,body], with no sorting required for the list.

## Requirements
- Implement `idempotency_key(method, url, body)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Canonicalize before hashing to avoid ambiguous keys.

## Run tests
`python -m pytest tests -q`
