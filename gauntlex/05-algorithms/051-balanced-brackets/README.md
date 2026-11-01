# Nested Delimiters

## Description
A sequence of brackets is valid only when every opening bracket has a matching closing bracket of the correct type and nesting order.

## Requirements
- Implement `balanced_brackets(text)` in `solution.py`.
- Return the required value without printing.
- Do not modify caller-owned input collections.
- Do not run input prompts or print statements at import time.

## Examples
`balanced_brackets("([]{})")` → `True`

`balanced_brackets("([)]")` → `False`

## Tips
Matching the total counts is not enough. Consider the order in which opening brackets must close.

The examples illustrate the contract without providing an implementation.
