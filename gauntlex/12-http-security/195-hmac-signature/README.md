# Authenticate a Message

## Description
Compute a keyed SHA-256 message authentication code for a message and shared secret.

### Behavior contract
Return lowercase HMAC-SHA256 hex digest of a UTF-8 message with a UTF-8 secret key.

## Requirements
- Implement `hmac_signature(secret, message)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`hmac_signature("key", "The quick brown fox jumps over the lazy dog")` → `"f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8"`

## Tips
A keyed MAC differs from an ordinary hash because it depends on the secret.

Examples describe the contract, not a solution.
