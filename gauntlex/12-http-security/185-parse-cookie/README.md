# parse_cookie

## Challenge
Parse a Cookie header string into a dictionary of cookie names to values. Trim spaces around names and values; ignore empty segments. Later duplicates overwrite earlier ones. Do not decode percent escapes.

## Requirements
- Implement `parse_cookie(text)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`parse_cookie("a=1; theme=dark")` → `{"a": "1", "theme": "dark"}`

`parse_cookie("a=1; a=2; ")` → `{"a": "2"}`

## Tips
Split cookie pairs on semicolons, then split each pair at the first equals sign.
