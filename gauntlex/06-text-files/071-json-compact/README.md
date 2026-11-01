# Canonical JSON Text

## Description
Serialize a Python value into stable, compact JSON with predictable key ordering.

## Requirements
- Implement `compact_json(value)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`compact_json({"b": 2, "a": 1})` → `"{\"a\":1,\"b\":2}"`

`compact_json([1, 2, 3])` → `"[1,2,3]"`

## Tips
Whitespace and key order affect the output string even when the underlying data is equivalent.

Examples describe expected behavior without providing the implementation.
