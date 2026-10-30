# derive_key

## Challenge
Return lowercase hex of a 32-byte PBKDF2-HMAC-SHA256 derived key for UTF-8 password and salt with positive integer iterations. Raise ValueError for nonpositive iterations.

## Requirements
- Implement `derive_key(password, salt, iterations)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
PBKDF2 deliberately repeats a keyed hash to slow guessing.

## Run tests
`python -m pytest tests -q`
