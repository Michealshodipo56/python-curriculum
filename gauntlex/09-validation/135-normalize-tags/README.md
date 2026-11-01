# Clean the Tags

## Description
Normalize comma-separated labels and remove duplicates without disturbing their first appearance.

### Behavior contract
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
Normalize a tag before deciding whether it is empty or has already appeared.

The examples specify results without giving an implementation.
