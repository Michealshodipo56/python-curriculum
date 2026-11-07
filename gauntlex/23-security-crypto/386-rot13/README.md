# Half an Alphabet

## Description

Apply a fixed alphabet rotation that reverses itself when applied twice.

## Requirements

- Implement `rot13(text)` in `starter/solution.py`.
- Apply ROT13 to ASCII letters only, preserving case and all other characters. Applying it twice restores the input.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Apply a fixed rotation of 13 positions to ASCII letters while preserving their case. Applying the operation a second time must restore the original string.

## Tips

Check that capitalization and punctuation survive unchanged.

## Example Behavior

`rot13('Hello, World!')` → `'Uryyb, Jbeyq!'`.
