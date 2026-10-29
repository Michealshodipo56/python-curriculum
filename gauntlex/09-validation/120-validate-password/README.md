# validate_password

## Description
Return True if a string has at least 8 characters and contains at least one ASCII uppercase letter, one ASCII lowercase letter, and one ASCII digit.

## Requirements
- Implement `validate_password(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`validate_password("Abcdefg1")` → `True`

`validate_password("abcdefg1")` → `False`

## Tips
Combine several independent character-class checks.
