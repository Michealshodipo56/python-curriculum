# json_value

## Description
Parse a JSON object string and return the value for the given key, or None when missing.

## Requirements
- Implement `json_value(text, key)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`json_value("{\"a\":1,\"b\":2}", "a")` → `1`

`json_value("{\"x\":null}", "x")` → `None`

## Tips
Use the JSON decoder before looking up the key.
