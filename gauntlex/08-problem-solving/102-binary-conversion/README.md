# Write in Base Two

## Description

Represent any integer using base-two digits. Return the representation as plain text without Python's binary prefix.

## Requirements

- Implement `to_binary(n)` in `starter/solution.py`.
- Return a string of binary digits representing integer `n`.
- For negative values, use a leading `-` followed by the magnitude's binary digits.
- Return `'0'` for zero.
- Do not include a `0b` prefix.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Why does zero need special attention?
- How does a negative sign relate to the digits of the magnitude?

## Example Behavior

`to_binary(0)` → `'0'`; `to_binary(13)` → `'1101'`; `to_binary(-5)` → `'-101'`.
