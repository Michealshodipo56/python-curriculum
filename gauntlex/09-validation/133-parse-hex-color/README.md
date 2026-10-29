# parse_hex_color

## Description
Parse a color string `#RRGGBB` into a tuple of three integers in [0,255]. Raise ValueError if the input is not exactly six hexadecimal digits after #.

## Requirements
- Implement `parse_hex_color(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_hex_color("#FF8000")` → `[255, 128, 0]`

`parse_hex_color("#000000")` → `[0, 0, 0]`

## Tips
Validate length and characters before decoding base 16.
