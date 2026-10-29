# valid_parentheses

## Description
Return True if a string containing only `(` and `)` is balanced, with no prefix containing more closing than opening brackets.

## Requirements
- Implement `valid_parentheses(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`valid_parentheses("(())")` → `True`

`valid_parentheses("())(")` → `False`

## Tips
A running balance must never become negative and must finish at zero.
