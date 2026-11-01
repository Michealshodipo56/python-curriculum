# First Unrepeated Character

## Description
Find the earliest character in a string that occurs exactly once across the entire string.

## Requirements
- Implement `first_unique(text)` in `solution.py`.
- Return the first character with frequency one, or `None` if none exists.
- Treat uppercase and lowercase characters as different.
- Return the result instead of printing it.
- Do not run input-handling code when the module is imported.

## Example
`first_unique('swiss')` → `'w'`; `first_unique('aabb')` → `None`.

## Tips
A character can look unique early on and repeat later. What information is needed before deciding?

The examples specify behavior without supplying the implementation.
