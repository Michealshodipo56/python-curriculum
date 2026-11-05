# Resolve a Link

## Description
Resolve a relative link against an absolute base URL using standard URL path rules.

## Requirements
- Implement `resolve_url(base, relative)` in `starter/solution.py`.
- Return the resolved absolute URL.
- Respect parent-directory paths, root-relative paths, and the base URL's trailing slash.
- Do not make network requests.
- Use the Python standard library, without printing or making network requests.

## Tips
- Why does a root-relative link behave differently from a parent-relative link?

## Example Behavior
`resolve_url("https://example.com/a/b", "../c")` → `"https://example.com/c"`

`resolve_url("https://example.com/a/", "/x")` → `"https://example.com/x"`
