# mask_secret

## Challenge
Return the last visible_count characters of secret prefixed with asterisks for hidden characters. If visible_count is zero, mask all characters. Require visible_count>=0.

## Requirements
- Implement `mask_secret(secret, visible_count)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Clamp visible characters to the length of the secret.

## Run tests
`python -m pytest tests -q`
