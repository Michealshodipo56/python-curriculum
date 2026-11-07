# Secure Random Token

## Description

Generate a URL-safe token from cryptographically secure random bytes.

## Requirements

- Implement `random_token(n)` in `starter/solution.py`.
- Return a URL-safe Base64 token representing exactly n cryptographically random bytes, without trailing padding. Require integer `n >= 1`; raise `ValueError` otherwise. Tests check format and decoded length, not a fixed random output.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Generate exactly the requested number of cryptographically secure random bytes before URL-safe Base64 encoding. Remove trailing padding, and never use predictable general-purpose randomness.

## Tips

A security token needs a secure randomness source, not a predictable pseudo-random sequence.

## Example Behavior

`random_token(16)` returns a URL-safe token whose Base64-decoded payload is exactly 16 bytes; `random_token(0)` is invalid.
