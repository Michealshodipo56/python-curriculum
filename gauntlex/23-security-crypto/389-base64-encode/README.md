# base64_encode

## Challenge
Return standard Base64 encoding of the UTF-8 bytes of text, including padding.

## Requirements
- Implement `base64_encode(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Base64 works on bytes, not directly on Unicode code points.

## Run tests
`python -m pytest tests -q`
