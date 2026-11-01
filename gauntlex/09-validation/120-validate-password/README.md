# Password Rules

## Description
Check a candidate password against several independent character and length requirements.

### Behavior contract
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
A long password can still fail if it lacks one required character class.

The examples show required behavior, not an implementation.
