# to_roman

## Description
Convert an integer from 1 to 3999 to its canonical uppercase Roman numeral representation.

## Requirements
- Implement `to_roman(n)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`to_roman(4)` → `"IV"`

`to_roman(58)` → `"LVIII"`

## Tips
Process place values from largest to smallest, including subtractive pairs.
