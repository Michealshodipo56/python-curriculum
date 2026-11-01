# Identify Duplicate Requests

## Description
Generate a stable key for logically identical requests using canonical input.

### Behavior contract
Given a method, URL, and request body string, return a stable lowercase SHA-256 hex digest of compact JSON encoding of [method.upper(),url,body], with no sorting required for the list.

## Requirements
- Implement `idempotency_key(method, url, body)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Canonical representation matters: concatenated fields can otherwise collide ambiguously.

Design your own implementation from the specified behavior.
