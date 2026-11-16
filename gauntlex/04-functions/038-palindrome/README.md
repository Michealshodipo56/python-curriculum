# Mirror Text

## Description

In `starter/solution.py`, write `is_palindrome(text)` to return `True` if the text reads exactly the same forward and backward, or `False` otherwise. For example, `racecar` is a palindrome. Capitalization and spaces count.

## Requirements

- Implement `is_palindrome(text)` in `starter/solution.py`.
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
