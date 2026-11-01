# Encode Base64

## Description
Represent UTF-8 text as standard Base64, including required padding.

### Behavior contract
Return standard Base64 encoding of the UTF-8 bytes of text, including padding.

## Requirements
- Implement `base64_encode(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Base64 encodes bytes and does not provide confidentiality.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
