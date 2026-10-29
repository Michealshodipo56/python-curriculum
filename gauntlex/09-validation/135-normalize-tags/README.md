# normalize_tags

## Description
Given a comma-separated string, return unique lowercase trimmed nonempty tags in first-appearance order.

## Requirements
- Implement `normalize_tags(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`normalize_tags("Python, python, AI, , ai")` → `["python", "ai"]`

`normalize_tags(" , ")` → `[]`

## Tips
Normalize each tag before checking whether it has appeared.
