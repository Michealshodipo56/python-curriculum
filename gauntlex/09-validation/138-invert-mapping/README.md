# Reverse a Relationship

## Description
Reverse a mapping while retaining all original keys that share one value.

### Behavior contract
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
An inverse is not necessarily one-to-one; a value can map back to several keys.

The examples specify results without giving an implementation.
