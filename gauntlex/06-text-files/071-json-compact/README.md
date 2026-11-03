# Canonical JSON Text

## Description
Serialize a Python value into stable, compact JSON with predictable key ordering.

## Requirements
- Implement `compact_json(value)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`compact_json({"b": 2, "a": 1})` → `"{\"a\":1,\"b\":2}"`

`compact_json([1, 2, 3])` → `"[1,2,3]"`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Whitespace and key order affect the output string even when the underlying data is equivalent.
