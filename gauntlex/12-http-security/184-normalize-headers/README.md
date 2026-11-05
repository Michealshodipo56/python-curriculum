# Canonical Header Names

## Description
HTTP header names are case-insensitive. Normalize them while retaining the latest supplied value.

## Requirements
- Implement `normalize_headers(pairs)` in `starter/solution.py`.
- Accept `[name, value]` pairs.
- Return a dictionary with trimmed lowercase names and trimmed values.
- Keep the last value when a normalized name repeats.
- Preserve value capitalization and do not mutate inputs.
- Use Python's standard library without printing or making network requests.

## Tips
- Why are header names and header values normalized differently?

## Example Behavior
`normalize_headers([["Content-Type", " text/plain "], ["X-KEY", " 1 "]])` → `{"content-type": "text/plain", "x-key": "1"}`

`normalize_headers([["X", "1"], ["x", "2"]])` → `{"x": "2"}`
