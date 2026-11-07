# Vowel Census

## Description
Count how many English vowels appear in a piece of text. The count must include repeated vowels and treat uppercase and lowercase forms equally.

## Requirements
- Implement `count_vowels(text)` in `solution.py`.
- Count occurrences of `a`, `e`, `i`, `o`, and `u`, regardless of case.
- Do not count `y` as a vowel.
- Return an integer, including zero for text without vowels.
- Do not print or execute input-handling code on import.

## Tips
- How can characters be compared consistently despite capitalization?
- Does counting distinct vowel types give the same result as counting occurrences?
- Consider an empty string.

## Example Behavior
`count_vowels('Gauntlex')` → `3`; `count_vowels('WHY')` → `0`.
