# hex_decode

## Challenge
Decode a hexadecimal string to UTF-8 text. Raise ValueError for odd-length or invalid hex, and UnicodeDecodeError for invalid UTF-8 bytes.

## Requirements
- Implement `hex_decode(hex_text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Separate byte decoding from UTF-8 decoding.

## Run tests
`python -m pytest tests -q`
