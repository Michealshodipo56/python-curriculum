# parse_query

## Description
Parse an HTTP-style query string into a dictionary mapping each key to its last value. Decode percent escapes and plus-as-space. Blank values are retained.

## Requirements
- Implement `parse_query(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_query("a=1&b=two+words&a=3")` → `{"a": "3", "b": "two words"}`

`parse_query("x=&y=%2B")` → `{"x": "", "y": "+"}`

## Tips
The standard library urllib.parse supports query parsing.
