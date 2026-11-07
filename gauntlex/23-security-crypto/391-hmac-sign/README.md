# Sign a Message

## Description
Create a keyed SHA-256 message authentication code using a shared secret.

## Requirements
- Implement `hmac_sign(secret, message)` in `starter/solution.py`.
- Return lowercase HMAC-SHA256 hex digest for UTF-8 message using UTF-8 secret key.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Use the standard library's HMAC-SHA256 implementation over UTF-8 secret and message bytes. Do not substitute a plain hash of concatenated strings for a keyed MAC.

## Tips
A message authentication code depends on both the key and message.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
Signing the same message with the same secret produces the same 64-character lowercase hexadecimal digest.
