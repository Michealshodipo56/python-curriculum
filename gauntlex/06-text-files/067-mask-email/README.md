# Protect the Address

## Description

Implement `mask_email(email)` in `starter/solution.py`. Preserve the domain and `@` separator in the returned address.

## Requirements

- Implement `mask_email(email)` in `starter/solution.py`.
- Preserve the domain and `@` separator in the returned address.
- For a local part longer than one character, keep its first character and replace each remaining character with `*`.
- Keep a one-character local part visible as shown in the examples.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.
- Assume a valid address with exactly one `@` and a nonempty local part and domain; email validation is outside this challenge.

## Tips

- **Concept to understand:** When displaying an address publicly, conceal most of the local part while keeping its first character and domain recognizable.
- Which characters identify the domain and must remain unchanged?
- How does the result differ for a one-character local part?

## Example Behavior

`mask_email("alice@example.com")` → `"a****@example.com"`

`mask_email("x@y.io")` → `"x@y.io"`
