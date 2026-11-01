# Shift the Alphabet

## Description
Implement a classical substitution cipher for ASCII letters while preserving all other text.

### Behavior contract
Shift ASCII letters by integer shift, wrapping within A-Z and a-z; leave other characters unchanged. Negative shifts are allowed.

## Requirements
- Implement `caesar_cipher(text, shift)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A classical cipher is an exercise in text transformation, not a secure way to protect secrets.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
