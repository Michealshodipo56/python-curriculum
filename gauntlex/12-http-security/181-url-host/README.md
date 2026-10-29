# url_host

## Challenge
Return the lowercase hostname of an absolute HTTP or HTTPS URL. Raise ValueError for missing hostname or unsupported schemes.

## Requirements
- Implement `url_host(url)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`url_host("https://Example.COM:8443/path")` → `"example.com"`

`url_host("http://localhost/x")` → `"localhost"`

## Tips
Use urlsplit; validate the scheme and hostname separately.
