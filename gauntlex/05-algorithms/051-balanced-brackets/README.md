# Nested Delimiters

## Description

Brackets must close in the reverse order in which they open. Determine whether a string has correctly matched and nested parentheses, square brackets, and braces.

## Requirements

- Implement `balanced_brackets(text)` in `starter/solution.py`.
- Recognize `()`, `[]`, and `{}` as matching pairs.
- Return `True` only when all brackets are correctly nested and closed.
- Ignore characters that are not brackets; an empty string is valid.
- Return a boolean without printing or executing code on import.

## Tips

- Why are equal counts of opening and closing brackets insufficient?
- Which opening bracket should match the next closing bracket?
- Consider mismatched nesting.

## Example Behavior

`balanced_brackets('([]{})')` → `True`; `balanced_brackets('([)]')` → `False`.
