# Derive a Key

## Description
Derive fixed-length key material from a password, salt, and iteration count.

### Behavior contract
Return lowercase hex of a 32-byte PBKDF2-HMAC-SHA256 derived key for UTF-8 password and salt with positive integer iterations. Raise ValueError for nonpositive iterations.

## Requirements
- Implement `derive_key(password, salt, iterations)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A key-derivation function deliberately repeats work; iterations must be positive.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
