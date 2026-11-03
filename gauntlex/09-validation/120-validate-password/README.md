# Password Rules

## Description
A password validator must check several independent conditions. Determine whether a candidate meets the required minimum length and ASCII character classes.

## Requirements
- Implement `validate_password(text)` in `starter/solution.py`.
- Return a Boolean for the supplied string.
- Require at least eight characters.
- Require at least one ASCII uppercase letter (`A`–`Z`), one ASCII lowercase letter (`a`–`z`), and one ASCII digit (`0`–`9`).
- Return `False` when any condition is missing.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why can a long password still be invalid?
- How are ASCII letters different from arbitrary Unicode letters?

## Example Behavior
`validate_password('Abcdefg1')` → `True`; `validate_password('abcdefg1')` → `False`.
