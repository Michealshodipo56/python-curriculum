# Reveal Only the End

## Description
Hide a secret's leading characters while allowing a specified number of trailing characters to remain visible.

### Behavior contract
Return the last visible_count characters of secret prefixed with asterisks for hidden characters. If visible_count is zero, mask all characters. Require visible_count>=0.

## Requirements
- Implement `mask_secret(secret, visible_count)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
The visible count can be zero or larger than the secret length.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
