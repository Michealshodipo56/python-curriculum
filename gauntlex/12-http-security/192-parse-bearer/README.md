# parse_bearer

## Challenge
Return the token from an Authorization header formatted as `Bearer TOKEN`, ignoring case of Bearer and allowing extra whitespace. Return None for invalid or empty tokens.

## Requirements
- Implement `parse_bearer(header)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`parse_bearer("Bearer abc123")` → `"abc123"`

`parse_bearer(" bearer   XYZ ")` → `"XYZ"`

## Tips
Validate the scheme and require exactly one token.
