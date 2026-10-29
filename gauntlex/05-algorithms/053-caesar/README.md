# caesar

## Description
Shift ASCII letters by integer k positions, wrapping within A-Z or a-z. Leave nonletters unchanged.

## Requirements
- Implement `caesar(text, k)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`caesar("Abc-Z!", 2)` → `"Cde-B!"`

`caesar("xyz", 3)` → `"abc"`

## Tips
Convert letters to alphabet positions, apply modular arithmetic, and restore the correct case.
