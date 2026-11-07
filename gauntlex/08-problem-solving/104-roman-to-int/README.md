# Numeral to Number

## Description

Interpret a canonical uppercase Roman numeral as its decimal integer value. Some symbols subtract from the following larger symbol rather than adding.

## Requirements

- Implement `roman_to_int(text)` in `starter/solution.py`.
- Assume `text` is a valid canonical uppercase Roman numeral.
- Return its integer value.
- Account for subtractive pairs without requiring validation of malformed input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- How can the symbol immediately following another affect its value?
- Consider the difference between `VI` and `IV`.

## Example Behavior

`roman_to_int('IV')` → `4`; `roman_to_int('LVIII')` → `58`.
