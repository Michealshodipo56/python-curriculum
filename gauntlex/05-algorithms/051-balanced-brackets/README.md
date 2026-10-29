# balanced_brackets

## Description
Return True if a string of only `()[]{}` brackets is properly nested and balanced.

## Requirements
- Implement `balanced_brackets(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`balanced_brackets("([]{})")` → `True`

`balanced_brackets("([)]")` → `False`

## Tips
A stack records opening brackets awaiting their matching close.
