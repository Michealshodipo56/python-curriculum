# Text to Hexadecimal

## Description
Encode UTF-8 text into a lowercase hexadecimal representation of its bytes.

### Behavior contract
Return lowercase hexadecimal representation of UTF-8 bytes of the input string, without spaces or prefix.

## Requirements
- Implement `hex_encode(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Unicode characters can occupy several bytes before hexadecimal encoding.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
