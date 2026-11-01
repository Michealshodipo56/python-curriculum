# Find a JSON Field

## Description
Interpret a JSON object and retrieve a value by key, accounting for keys that are absent.

## Requirements
- Implement `json_value(text, key)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`json_value("{\"a\":1,\"b\":2}", "a")` → `1`

`json_value("{\"x\":null}", "x")` → `None`

## Tips
JSON `null` and a missing key can lead to the same Python result; understand the specified contract.

Examples describe expected behavior without providing the implementation.
