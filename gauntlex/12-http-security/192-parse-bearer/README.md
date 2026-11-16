# Read a Bearer Token

## Description

Implement `parse_bearer(header)` in `starter/solution.py`. Recognize `Bearer TOKEN` without regard to scheme capitalization.

## Requirements

- Implement `parse_bearer(header)` in `starter/solution.py`.
- Recognize `Bearer TOKEN` without regard to scheme capitalization.
- Allow extra surrounding and separating whitespace.
- Return the token as written.
- Return `None` for missing tokens, invalid schemes, or malformed headers.
- Use Python's standard library without printing or making network requests.

## Tips

- **Concept to understand:** Extract one token from an Authorization header while checking its authentication scheme.
- Why must the scheme be validated before accepting the token?

## Example Behavior

`parse_bearer("Bearer abc123")` → `"abc123"`

`parse_bearer(" bearer   XYZ ")` → `"XYZ"`
