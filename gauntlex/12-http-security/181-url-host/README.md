# Identify the Host

## Description
Extract the hostname of an absolute web URL while rejecting unsupported schemes and missing hosts.

### Behavior contract
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
A URL's hostname is not its entire network location: ports and paths are separate.

Examples describe the contract, not a solution.
