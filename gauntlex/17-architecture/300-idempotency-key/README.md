# Identify Duplicate Requests

## Description
Logically identical requests need a stable identifier even when their method capitalization differs. Canonicalize request data before hashing.

## Requirements
- Implement `idempotency_key(method, url, body)` in `starter/solution.py`.
- Accept a method, URL, and request body string.
- Uppercase the method.
- Serialize `[method, url, body]` as compact JSON in that order.
- Hash the UTF-8 JSON bytes with SHA-256.
- Return the lowercase hexadecimal digest.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The JSON array field order matters. Method case is normalized, but URL and body text remain unchanged.

## Tips
- Why is structured serialization safer than concatenating fields?

## Example Behavior
Requests with methods `'post'` and `'POST'` and otherwise identical inputs must produce the same key.
