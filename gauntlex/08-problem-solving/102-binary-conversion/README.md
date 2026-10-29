# to_binary

## Description
Return the base-2 representation of an integer as a string, with a leading minus sign for negative values. Do not prefix 0b.

## Requirements
- Implement `to_binary(n)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`to_binary(0)` → `"0"`

`to_binary(13)` → `"1101"`

## Tips
Repeated division by two produces binary digits in reverse order.
