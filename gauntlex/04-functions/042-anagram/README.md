# Same Letters, Different Order

## Description

Two strings are anagrams when they contain the same characters with the same frequencies, even if their orders differ. Write a function that checks this exact relationship.

## Requirements

- Implement `are_anagrams(a, b)` in `starter/solution.py`.
- Return `True` when both strings have identical character frequencies.
- Treat uppercase and lowercase as different characters.
- Include spaces and punctuation in the comparison.
- Return a boolean without printing or executing input-handling code on import.

## Tips

- Why is comparing only the set of characters insufficient?
- What happens when one letter appears twice in one string?
- Consider strings of different lengths.

## Example Behavior

`are_anagrams('listen', 'silent')` → `True`; `are_anagrams('aab', 'abb')` → `False`.
