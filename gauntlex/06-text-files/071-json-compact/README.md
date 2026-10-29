# compact_json

## Description
Return compact JSON for a serializable Python value with sorted keys and no spaces after separators.

## Requirements
- Implement `compact_json(value)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`compact_json({"b": 2, "a": 1})` → `"{\"a\":1,\"b\":2}"`

`compact_json([1, 2, 3])` → `"[1,2,3]"`

## Tips
The JSON encoder accepts separators and sorting options.
