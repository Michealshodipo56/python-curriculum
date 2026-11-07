# Append Structured Records

## Description
JSON Lines stores independent JSON values on separate lines. Append a new value without destroying existing records.

## Requirements
- Implement `append_jsonl(path, value)` in `starter/solution.py`.
- Open or create the UTF-8 file at `path` for appending.
- Serialize the JSON-compatible value in compact JSON with sorted object keys.
- Append exactly one serialized record followed by a newline.
- Return `None` and preserve existing content.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why must each appended value end with a newline?

## Example Behavior
Appending `{'b': 2, 'a': 1}` writes `{"a":1,"b":2}\n` at the end of the file.
