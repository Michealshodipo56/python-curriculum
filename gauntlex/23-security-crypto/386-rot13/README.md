# Half an Alphabet

## Description
Apply a fixed alphabet rotation that reverses itself when applied twice.

### Behavior contract
Apply ROT13 to ASCII letters only, preserving case and all other characters. Applying it twice restores the input.

## Requirements
- Implement `rot13(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Check that capitalization and punctuation survive unchanged.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
