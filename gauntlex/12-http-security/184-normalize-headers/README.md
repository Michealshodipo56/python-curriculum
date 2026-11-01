# Canonical Header Names

## Description
Normalize a sequence of HTTP headers while retaining the latest value for duplicate names.

### Behavior contract
Given a sequence of [name,value] HTTP header pairs, return a dictionary with lowercase trimmed names and trimmed values. Later duplicate names overwrite earlier values.

## Requirements
- Implement `normalize_headers(pairs)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`normalize_headers([["Content-Type", " text/plain "], ["X-KEY", " 1 "]])` → `{"content-type": "text/plain", "x-key": "1"}`

`normalize_headers([["X", "1"], ["x", "2"]])` → `{"x": "2"}`

## Tips
HTTP header names are case-insensitive, but their values are not necessarily so.

Examples describe the contract, not a solution.
