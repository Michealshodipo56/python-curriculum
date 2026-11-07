# Derive a Key

## Description

Derive fixed-length key material from a password, salt, and iteration count.

## Requirements

- Implement `derive_key(password, salt, iterations)` in `starter/solution.py`.
- Return lowercase hex of a 32-byte PBKDF2-HMAC-SHA256 derived key for UTF-8 password and salt with positive integer iterations. Raise ValueError for nonpositive iterations.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Use PBKDF2-HMAC-SHA256 from the standard library with the requested positive iteration count and a 32-byte derived key. Encode the final key as lowercase hexadecimal.

## Tips

A key-derivation function deliberately repeats work; iterations must be positive.

## Example Behavior

For valid inputs, `derive_key('pass', 'salt', 1000)` returns a deterministic 64-character lowercase hexadecimal string; zero iterations raises `ValueError`.
