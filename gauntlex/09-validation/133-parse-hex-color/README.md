# Decode an RGB Color

## Description
A six-digit hexadecimal color stores red, green, and blue intensities in three adjacent pairs. Validate and decode each channel.

## Requirements
- Implement `parse_hex_color(text)` in `starter/solution.py`.
- Accept exactly `#RRGGBB` where each letter is a hexadecimal digit.
- Reject missing `#`, incorrect lengths, and nonhexadecimal characters with `ValueError`.
- Return three integer channel values between `0` and `255`, in red-green-blue order.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why does each color channel occupy two hexadecimal digits?
- Why should the full input be validated before decoding?

## Example Behavior
`parse_hex_color('#FF8000')` → `[255, 128, 0]`; `parse_hex_color('#000000')` → `[0, 0, 0]`.
