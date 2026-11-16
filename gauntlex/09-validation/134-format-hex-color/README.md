# Encode an RGB Color

## Description

Implement `format_hex_color(r, g, b)` in `starter/solution.py`. Require every component to lie between `0` and `255`; raise `ValueError` otherwise.

## Requirements

- Implement `format_hex_color(r, g, b)` in `starter/solution.py`.
- Accept three integer channel values `r`, `g`, and `b`.
- Require every component to lie between `0` and `255`; raise `ValueError` otherwise.
- Return a string in uppercase `#RRGGBB` form.
- Represent each channel with exactly two hexadecimal digits.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- **Concept to understand:** Encode red, green, and blue channel values as a canonical uppercase hexadecimal color string.
- Why do small channel values still require two digits?
- How does channel order affect the resulting color?

## Example Behavior

`format_hex_color(255, 128, 0)` → `'#FF8000'`; `format_hex_color(0, 0, 0)` → `'#000000'`.
