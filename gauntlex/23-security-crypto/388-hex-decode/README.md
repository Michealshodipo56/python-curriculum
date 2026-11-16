# Hexadecimal to Text

## Description

Implement `hex_decode(hex_text)` in `starter/solution.py`. Decode a hexadecimal string to UTF-8 text. Raise ValueError for odd-length or invalid hex, and UnicodeDecodeError for invalid UTF-8 bytes.

## Requirements

- Implement `hex_decode(hex_text)` in `starter/solution.py`.
- Decode a hexadecimal string to UTF-8 text. Raise ValueError for odd-length or invalid hex, and UnicodeDecodeError for invalid UTF-8 bytes.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Validate hexadecimal syntax and decode bytes as UTF-8, distinguishing invalid hex text from invalid Unicode byte sequences. Do not silently replace decoding errors.

## Tips

- **Concept to understand:** Decode hexadecimal bytes into UTF-8 text with clear failures for invalid input.
Invalid hexadecimal syntax and invalid UTF-8 are different error conditions.

## Example Behavior

`hex_decode('4869')` → `'Hi'`; `hex_decode('f')` raises `ValueError`.
