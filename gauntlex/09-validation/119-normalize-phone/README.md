# normalize_phone

## Description
Remove spaces, hyphens and parentheses from a phone string. Keep an optional leading +. Raise ValueError if any other character remains or no digits remain.

## Requirements
- Implement `normalize_phone(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`normalize_phone("+1 (555) 123-4567")` → `"+15551234567"`

`normalize_phone("080-123 456")` → `"080123456"`

## Tips
Validate characters before or after removing allowed separators.
