# First Unrepeated Character

## Description

A character that appears once may be useful as a unique marker. Find the earliest character whose total frequency in the complete string is exactly one.

## Requirements

- Implement `first_unique(text)` in `starter/solution.py`.
- Return the first character occurring exactly once in the entire string.
- Return `None` when no such character exists.
- Treat uppercase and lowercase characters as distinct.
- Do not print or execute input-handling code on import.

## Tips

- Why might a character that seems unique at first turn out to repeat later?
- How can frequency and original order both matter?
- Consider empty input.

## Example Behavior

`first_unique('swiss')` → `'w'`; `first_unique('aabb')` → `None`.
