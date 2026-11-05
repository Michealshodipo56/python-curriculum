# Assemble a Cookie Header

## Description
Serialize cookie pairs into a predictable header string.

## Requirements
- Implement `build_cookie(cookies)` in `starter/solution.py`.
- Assume valid cookie names and values.
- Sort names alphabetically and join `name=value` entries with `; `.
- Return an empty string for an empty mapping.
- Use Python's standard library without printing or making network requests.

## Tips
- Why does a stable ordering help reproducibility?

## Example Behavior
`build_cookie({"theme": "dark", "a": "1"})` → `"a=1; theme=dark"`

`build_cookie({})` → `""`
