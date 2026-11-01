# Shared Dictionary Keys

## Description
Compare two mappings and list the keys present in both.

### Behavior contract
Return a sorted list of keys appearing in both input dictionaries.

## Requirements
- Implement `common_keys(a, b)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`common_keys({"x": 1, "a": 2}, {"a": 3, "z": 4})` → `["a"]`

`common_keys({}, {"x": 1})` → `[]`

## Tips
A stable alphabetical result should not depend on insertion order.

The examples specify results without giving an implementation.
