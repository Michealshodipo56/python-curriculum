# Decode Base64

## Description
Decode strictly validated Base64 text back into Unicode.

### Behavior contract
Decode standard Base64 text to UTF-8. Reject invalid Base64 characters or padding with ValueError. Propagate UnicodeDecodeError for invalid UTF-8.

## Requirements
- Implement `base64_decode(encoded)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Malformed padding and invalid decoded UTF-8 must not be silently accepted.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
