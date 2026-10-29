# hmac_signature

## Challenge
Return lowercase HMAC-SHA256 hex digest of a UTF-8 message with a UTF-8 secret key.

## Requirements
- Implement `hmac_signature(secret, message)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`hmac_signature("key", "The quick brown fox jumps over the lazy dog")` → `"f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8"`

## Tips
The hmac module accepts a digest algorithm name.
