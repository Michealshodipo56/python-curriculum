# Find a JSON Field

## Description
Interpret a JSON object and retrieve a value by key, accounting for keys that are absent.

## Requirements
- Implement `json_value(text, key)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`json_value("{\"a\":1,\"b\":2}", "a")` → `1`

`json_value("{\"x\":null}", "x")` → `None`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
JSON `null` and a missing key can lead to the same Python result; understand the specified contract.
