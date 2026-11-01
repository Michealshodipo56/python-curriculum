# Protect the Address

## Description
Hide the sensitive portion of an email address while leaving enough information to recognize its structure.

## Requirements
- Implement `mask_email(email)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`mask_email("alice@example.com")` → `"a****@example.com"`

`mask_email("x@y.io")` → `"x@y.io"`

## Tips
Which part of the address should remain untouched? Consider a one-character local part.

Examples describe expected behavior without providing the implementation.
