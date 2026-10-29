# normalize_headers

## Challenge
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
Header field names are case-insensitive.
