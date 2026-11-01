# Append Structured Records

## Description
Add one JSON value to a JSON Lines file while keeping earlier records intact.

### Behavior contract
Append a JSON-compatible value as one compact sorted-key JSON record followed by a newline to a UTF-8 file, creating it if absent. Return None.

## Requirements
- Implement `append_jsonl(path, value)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Each appended record occupies its own line.

The task defines behavior; design the implementation independently.
