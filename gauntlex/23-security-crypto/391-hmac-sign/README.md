# Sign a Message

## Description
Create a keyed SHA-256 message authentication code using a shared secret.

### Behavior contract
Return lowercase HMAC-SHA256 hex digest for UTF-8 message using UTF-8 secret key.

## Requirements
- Implement `hmac_sign(secret, message)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A message authentication code depends on both the key and message.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
