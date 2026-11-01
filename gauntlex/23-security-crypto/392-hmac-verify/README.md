# Authenticate a Signature

## Description
Verify a message authentication code without leaking the first mismatching position.

### Behavior contract
Return True only if lowercase or uppercase hexadecimal signature equals the HMAC-SHA256 signature of UTF-8 message with UTF-8 secret. Reject malformed signatures by returning False. Use constant-time comparison.

## Requirements
- Implement `hmac_verify(secret, message, signature)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Reject malformed signatures before using a timing-resistant comparison.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
