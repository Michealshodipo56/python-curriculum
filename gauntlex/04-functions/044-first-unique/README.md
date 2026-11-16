# First Unrepeated Character

## Description

In `starter/solution.py`, write `first_unique(text)` to return the first character that occurs **only once** in the entire string. If every character repeats, return `None`. Treat uppercase and lowercase letters as different.

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
