# Alphabet Rotation

## Description
Transform text by shifting each ASCII letter around its alphabet. Preserve case, punctuation, digits, and other nonletters.

## Requirements
- Implement `caesar(text, k)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`caesar("Abc-Z!", 2)` → `"Cde-B!"`

`caesar("xyz", 3)` → `"abc"`

## Tips
Investigate what happens at the end of the alphabet and with shifts larger than its length.

The examples illustrate the contract without providing an implementation.
