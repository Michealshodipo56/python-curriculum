# Hexadecimal to Text

## Description
Decode hexadecimal bytes into UTF-8 text with clear failures for invalid input.

### Behavior contract
Decode a hexadecimal string to UTF-8 text. Raise ValueError for odd-length or invalid hex, and UnicodeDecodeError for invalid UTF-8 bytes.

## Requirements
- Implement `hex_decode(hex_text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Invalid hexadecimal syntax and invalid UTF-8 are different error conditions.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
