# Encode an RGB Color

## Description
Convert three channel values into a canonical uppercase hexadecimal color string.

### Behavior contract
Return an uppercase `#RRGGBB` string for three integer RGB components. Raise ValueError if any component is outside 0–255.

## Requirements
- Implement `format_hex_color(r, g, b)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`format_hex_color(255, 128, 0)` → `"#FF8000"`

`format_hex_color(0, 0, 0)` → `"#000000"`

## Tips
Each channel needs exactly two hexadecimal digits, even for small values.

The examples specify results without giving an implementation.
