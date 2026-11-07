# Authenticate a Signature

## Description

Verify a message authentication code without leaking the first mismatching position.

## Requirements

- Implement `hmac_verify(secret, message, signature)` in `starter/solution.py`.
- Return True only if lowercase or uppercase hexadecimal signature equals the HMAC-SHA256 signature of UTF-8 message with UTF-8 secret. Reject malformed signatures by returning False. Use constant-time comparison.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Validate the supplied hexadecimal signature before comparison, accept upper- or lowercase hex, and use a timing-resistant equality primitive for the expected MAC.

## Tips

Reject malformed signatures before using a timing-resistant comparison.

## Example Behavior

A signature produced by `hmac_sign('key', 'message')` verifies for the same secret and message; a changed message returns `False`.
