# Escape One URL Component

## Description
Encode arbitrary UTF-8 text as one URL path component, including slashes and spaces.

### Behavior contract
Percent-encode a UTF-8 string for use as one URL path component. Keep only RFC 3986 unreserved characters unescaped and encode spaces as %20.

## Requirements
- Implement `encode_component(text)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`encode_component("hello world")` → `"hello%20world"`

`encode_component("a/b")` → `"a%2Fb"`

## Tips
A slash inside a component must not become a path separator.

Examples describe the contract, not a solution.
