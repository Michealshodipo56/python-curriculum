# Compact JSON Text

## Description

A consistently formatted JSON representation makes output stable for comparison and storage. Convert JSON-compatible Python values into compact text with predictable object key order.

## Requirements

- Implement `compact_json(value)` in `starter/solution.py`.
- Serialize the supplied JSON-compatible value as a string, not bytes.
- Sort dictionary keys and omit unnecessary spaces between JSON tokens.
- Preserve the data's JSON meaning, including nested values and arrays.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.
- Use the standard JSON encoder's default escaping of non-ASCII characters; dictionary keys are strings and numeric values are finite.

## Tips

- Why can two equivalent dictionaries serialize differently without canonical key ordering?
- Which spaces are structural formatting rather than part of string values?

## Example Behavior

`compact_json({"b": 2, "a": 1})` → `"{\"a\":1,\"b\":2}"`

`compact_json([1, 2, 3])` → `"[1,2,3]"`
