# Numeral to Number

## Description
Interpret a valid Roman numeral as an integer, including subtractive pairs.

### Behavior contract
Convert a valid canonical uppercase Roman numeral to its integer value. Input is guaranteed valid.

## Requirements
- Implement `roman_to_int(text)` in `starter/solution.py`.
- Return the result without printing or reading input.
- Do not mutate input collections.
- Use only Python's standard library.

## Examples
`roman_to_int("IV")` → `4`

`roman_to_int("LVIII")` → `58`

## Tips
The meaning of a symbol can depend on the symbol immediately following it.

The examples define expected behavior; design your own implementation.
