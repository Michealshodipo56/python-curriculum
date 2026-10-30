# caesar_cipher

## Challenge
Shift ASCII letters by integer shift, wrapping within A-Z and a-z; leave other characters unchanged. Negative shifts are allowed.

## Requirements
- Implement `caesar_cipher(text, shift)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Reduce the shift modulo the alphabet length.

## Run tests
`python -m pytest tests -q`
