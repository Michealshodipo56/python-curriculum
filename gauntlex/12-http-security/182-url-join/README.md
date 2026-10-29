# resolve_url

## Challenge
Resolve a possibly relative URL against an absolute base URL using standard URL resolution rules.

## Requirements
- Implement `resolve_url(base, relative)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`resolve_url("https://example.com/a/b", "../c")` → `"https://example.com/c"`

`resolve_url("https://example.com/a/", "/x")` → `"https://example.com/x"`

## Tips
The standard library can resolve relative URLs, including parent segments.
