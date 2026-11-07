# Reveal Only the End

## Description

Hide a secret's leading characters while allowing a specified number of trailing characters to remain visible.

## Requirements

- Implement `mask_secret(secret, visible_count)` in `starter/solution.py`.
- Return the last visible_count characters of secret prefixed with asterisks for hidden characters. If visible_count is zero, mask all characters. Require integer `visible_count >= 0`; raise `ValueError` otherwise.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Preserve only the requested trailing characters and replace each hidden character with an asterisk. A zero visible count hides everything; a count beyond the length hides nothing.

## Tips

The visible count can be zero or larger than the secret length.

## Example Behavior

`mask_secret('abcdef', 2)` → `'****ef'`; `mask_secret('abc', 0)` → `'***'`.
