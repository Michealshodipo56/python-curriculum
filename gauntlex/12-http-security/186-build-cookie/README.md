# build_cookie

## Challenge
Given a mapping of cookie names to values, return a Cookie header with keys in alphabetical order, formatted as `key=value` pairs separated by `; `. Assume valid names and values.

## Requirements
- Implement `build_cookie(cookies)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`build_cookie({"theme": "dark", "a": "1"})` → `"a=1; theme=dark"`

`build_cookie({})` → `""`

## Tips
Sort keys to ensure deterministic output.
