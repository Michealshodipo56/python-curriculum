# Telephone Canonical Form

## Description

Remove permitted visual separators from a telephone number without silently accepting invalid symbols. Preserve a plus sign only when it indicates an international prefix.

## Requirements

- Implement `normalize_phone(text)` in `starter/solution.py`.
- Remove spaces, hyphens, and parentheses.
- Preserve an optional `+` only at the beginning of the normalized number.
- Require at least one digit and reject every remaining character that is not a digit.
- Raise `ValueError` for invalid input.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why must a plus sign be checked for its position?
- Can removing formatting characters hide an invalid symbol?

## Example Behavior

`normalize_phone('+1 (555) 123-4567')` → `'+15551234567'`; `normalize_phone('080-123 456')` → `'080123456'`.
