# invert_mapping

## Description
Given a dictionary mapping strings to strings, return a dictionary mapping each value to the list of original keys in their insertion order.

## Requirements
- Implement `invert_mapping(mapping)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`invert_mapping({"a": "x", "b": "y", "c": "x"})` → `{"x": ["a", "c"], "y": ["b"]}`

`invert_mapping({})` → `{}`

## Tips
Multiple keys can share the same value, so each inverted entry needs a list.
