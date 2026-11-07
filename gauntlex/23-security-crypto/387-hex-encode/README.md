# Text to Hexadecimal

## Description
Encode UTF-8 text into a lowercase hexadecimal representation of its bytes.

## Requirements
- Implement `hex_encode(text)` in `starter/solution.py`.
- Return lowercase hexadecimal representation of UTF-8 bytes of the input string, without spaces or prefix.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Encode the input as UTF-8 bytes before converting each byte to hexadecimal. Unicode characters may occupy more than one byte, so do not encode code points directly.

## Tips
Unicode characters can occupy several bytes before hexadecimal encoding.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`hex_encode('Hi')` → `'4869'`; `hex_encode('é')` → `'c3a9'`.
