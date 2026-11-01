# Read Cookie Pairs

## Description
Interpret cookie header pairs into a mapping without accidentally decoding their content.

### Behavior contract
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
The equals sign can be part of a value; split each pair only at the first separator.

Examples describe the contract, not a solution.
