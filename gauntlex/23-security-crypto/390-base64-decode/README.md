# base64_decode

## Challenge
Decode standard Base64 text to UTF-8. Reject invalid Base64 characters or padding with ValueError. Propagate UnicodeDecodeError for invalid UTF-8.

## Requirements
- Implement `base64_decode(encoded)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Use strict Base64 validation before UTF-8 decoding.

## Run tests
`python -m pytest tests -q`
