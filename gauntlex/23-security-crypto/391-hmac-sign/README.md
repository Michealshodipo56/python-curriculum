# hmac_sign

## Challenge
Return lowercase HMAC-SHA256 hex digest for UTF-8 message using UTF-8 secret key.

## Requirements
- Implement `hmac_sign(secret, message)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
HMAC uses a keyed cryptographic hash.

## Run tests
`python -m pytest tests -q`
