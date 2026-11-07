# Authenticate a Message

## Description
A keyed message authentication code helps verify that a message came from someone holding a shared secret. Produce an HMAC using SHA-256 without exposing the key.

## Requirements
- Implement `hmac_signature(secret, message)` in `starter/solution.py`.
- Encode the secret and message separately as UTF-8.
- Return the lowercase hexadecimal HMAC-SHA256 digest.
- Treat the secret as the authentication key, not as an ordinary prefix or suffix.
- Do not print or expose the secret.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why does a keyed MAC provide different guarantees from an unkeyed hash?
- How would changing the secret affect the result?

## Example Behavior
`hmac_signature("key", "The quick brown fox jumps over the lazy dog")` → `"f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8"`
