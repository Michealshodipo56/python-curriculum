# Alphabet Rotation

## Description

Shift each English letter by a specified number of positions, wrapping around the alphabet. Preserve case and leave nonletters unchanged.

## Requirements

- Implement `caesar(text, k)` in `starter/solution.py`.
- Shift ASCII letters `A`–`Z` and `a`–`z` forward by integer `k` positions.
- Wrap around each alphabet; support zero, negative, and large shifts.
- Preserve case and leave all non-ASCII letters, digits, spaces, and punctuation unchanged.
- Return the transformed string without printing or executing code on import.

## Tips

- What happens when a shift crosses `z` or `Z`?
- How does a full alphabet rotation affect the result?
- Think about negative shifts.

## Example Behavior

`caesar('Abc-Z!', 2)` → `'Cde-B!'`; `caesar('xyz', 3)` → `'abc'`.
