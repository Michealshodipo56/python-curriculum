# sha256_hex

## Challenge
Return the lowercase SHA-256 hex digest of a UTF-8 string.

## Requirements
- Implement `sha256_hex(text)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`sha256_hex("")` → `"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`

`sha256_hex("abc")` → `"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"`

## Tips
Hash the UTF-8 encoded bytes, not the Python string object.
