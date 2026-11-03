# Protect the Address

## Description
Hide the sensitive portion of an email address while leaving enough information to recognize its structure.

## Requirements
- Implement `mask_email(email)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`mask_email("alice@example.com")` → `"a****@example.com"`

`mask_email("x@y.io")` → `"x@y.io"`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Which part of the address should remain untouched? Consider a one-character local part.
