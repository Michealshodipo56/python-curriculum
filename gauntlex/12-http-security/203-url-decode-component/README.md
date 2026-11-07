# Restore One URL Component

## Description
Recover text from percent-escaped UTF-8 bytes while preserving literal plus signs, which are not spaces in URL path components.

## Requirements
- Implement `decode_component(text)` in `starter/solution.py`.
- Percent-decode the input and interpret the resulting bytes as UTF-8.
- Do not convert literal `+` characters to spaces.
- Preserve unescaped characters as appropriate.
- Return the decoded string.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why does form-style query decoding handle plus signs differently?
- What happens to `%2F` during decoding?

## Example Behavior
`decode_component("hello%20world")` → `"hello world"`

`decode_component("a%2Fb")` → `"a/b"`
