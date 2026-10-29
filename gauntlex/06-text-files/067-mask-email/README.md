# mask_email

## Description
Given an email with one @ and nonempty local part, mask all local-part characters except the first with *.

## Requirements
- Implement `mask_email(email)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`mask_email("alice@example.com")` → `"a****@example.com"`

`mask_email("x@y.io")` → `"x@y.io"`

## Tips
Split at @ and rebuild the address.
