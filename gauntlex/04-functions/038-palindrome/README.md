# Mirror Text

## Description
Some strings read the same forward and backward. Build a function that checks this property using an exact character comparison; capitalization, spaces, and punctuation all matter.

## Requirements
- Implement `is_palindrome(text)` in `solution.py`.
- Return a boolean indicating whether the string reads identically in both directions.
- Compare characters exactly, including case and whitespace.
- Treat the empty string and a one-character string as palindromes.
- Do not print or execute input-handling code on import.

## Tips
- What positions correspond when reading from opposite ends?
- How would a single differing character affect the answer?
- Check strings with spaces and mixed case.

## Example Behavior
`is_palindrome('level')` → `True`; `is_palindrome('Level')` → `False`.
