# Identify the Host

## Description
An absolute web URL contains a scheme, a network location, and an optional path. Extract the hostname without confusing it with the port or the complete address.

## Requirements
- Implement `url_host(url)` in `starter/solution.py`.
- Accept an absolute HTTP or HTTPS URL.
- Return its hostname in lowercase, excluding the port and path.
- Raise `ValueError` for unsupported schemes or a missing hostname.
- Return the result without printing or making network requests.

## Tips
- Consider how a hostname differs from a network location containing a port.
- A URL may have a path without changing its hostname.

## Example Behavior
`url_host("https://Example.COM:8443/path")` → `"example.com"`

`url_host("http://localhost/x")` → `"localhost"`
