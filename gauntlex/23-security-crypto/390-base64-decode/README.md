# Decode Base64

## Description
Decode strictly validated Base64 text back into Unicode.

## Requirements
- Implement `base64_decode(encoded)` in `starter/solution.py`.
- Decode standard Base64 text to UTF-8. Reject invalid Base64 characters or padding with ValueError. Propagate UnicodeDecodeError for invalid UTF-8.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Reject malformed Base64 characters and padding instead of permissively discarding them. After decoding bytes, propagate any UTF-8 decoding error.

## Tips
Malformed padding and invalid decoded UTF-8 must not be silently accepted.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`base64_decode('SGk=')` → `'Hi'`; malformed Base64 raises `ValueError`.
