# allowed_origin

## Challenge
Return True if origin exactly matches one of the allowed origins. Scheme and port matter; do not accept suffix or prefix matches.

## Requirements
- Implement `allowed_origin(origin, allowed)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`allowed_origin("https://example.com", ["https://example.com"])` → `True`

`allowed_origin("https://evil-example.com", ["https://example.com"])` → `False`

## Tips
Compare full origin strings rather than using substring matching.
