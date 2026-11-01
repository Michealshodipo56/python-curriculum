# Write URL Parameters

## Description
Produce a predictable, encoded query string from a mapping of names and values.

### Behavior contract
Encode a mapping of string keys and values as an HTTP query string. Sort keys alphabetically before encoding. Use plus for spaces.

## Requirements
- Implement `build_query(params)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`build_query({"b": "two words", "a": "1"})` → `"a=1&b=two+words"`

`build_query({})` → `""`

## Tips
Sorting names first makes the result stable regardless of mapping insertion order.

The examples show required behavior, not an implementation.
