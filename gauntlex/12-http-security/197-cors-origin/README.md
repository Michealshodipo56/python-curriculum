# Exact Origin Allowlist

## Description
Cross-origin access decisions depend on exact origins, not vaguely similar hostnames. Check whether a request origin is explicitly permitted.

## Requirements
- Implement `allowed_origin(origin, allowed)` in `starter/solution.py`.
- Return `True` only when `origin` exactly equals one of the allowed origins.
- Treat URL scheme and port as significant.
- Do not accept substring, prefix, or suffix matches.
- Return `False` for an empty allowlist.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why is a lookalike domain not the same origin?
- What changes when an HTTPS origin uses a different port?

## Example Behavior
`allowed_origin("https://example.com", ["https://example.com"])` → `True`

`allowed_origin("https://evil-example.com", ["https://example.com"])` → `False`
