# Balance the Parentheses

## Description

Implement `valid_parentheses(text)` in `starter/solution.py`. Return `True` only if the parentheses form complete, correctly ordered pairs.

## Requirements

- Implement `valid_parentheses(text)` in `starter/solution.py`.
- Assume `text` contains only `(` and `)` characters.
- Return `True` only if the parentheses form complete, correctly ordered pairs.
- Return `True` for an empty string.
- Return a boolean without printing or executing code on import.

## Tips

- **Concept to understand:** A sequence of parentheses is valid only if every opening parenthesis is closed in the correct order. Detect invalid prefixes as well as unclosed parentheses at the end.
- Why can equal counts still describe an invalid sequence?
- What must remain true at every point while reading from left to right?

## Example Behavior

`valid_parentheses('(())')` → `True`; `valid_parentheses('())(')` → `False`.
