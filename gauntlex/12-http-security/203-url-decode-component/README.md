# decode_component

## Challenge
Percent-decode a URL component using UTF-8. Do not treat plus signs as spaces.

## Requirements
- Implement `decode_component(text)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`decode_component("hello%20world")` → `"hello world"`

`decode_component("a%2Fb")` → `"a/b"`

## Tips
Choose the decoder that does not implement form-style plus conversion.
