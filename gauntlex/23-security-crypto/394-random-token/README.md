# Secure Random Token

## Description
Generate a URL-safe token from cryptographically secure random bytes.

### Behavior contract
Return a URL-safe Base64 token representing exactly n cryptographically random bytes, without trailing padding. Require n>=1. Tests check format and decoded length, not a fixed random output.

## Requirements
- Implement `random_token(n)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A security token needs a secure randomness source, not a predictable pseudo-random sequence.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
