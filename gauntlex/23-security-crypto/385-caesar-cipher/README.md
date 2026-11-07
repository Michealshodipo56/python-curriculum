# Shift the Alphabet

## Description
Implement a classical substitution cipher for ASCII letters while preserving all other text.

## Requirements
- Implement `caesar_cipher(text, shift)` in `starter/solution.py`.
- Shift ASCII letters by integer shift, wrapping within A-Z and a-z; leave other characters unchanged. Negative shifts are allowed.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Transform ASCII letters independently within their uppercase and lowercase alphabets; punctuation, digits, and non-ASCII characters must remain unchanged.

## Tips
A classical cipher is an exercise in text transformation, not a secure way to protect secrets.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`caesar_cipher('Az-9', 1)` → `'Ba-9'`; `caesar_cipher('Ba', -1)` → `'Az'`.
