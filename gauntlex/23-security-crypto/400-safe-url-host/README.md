# safe_url_host

## Challenge
Return lowercase hostname from an absolute HTTP or HTTPS URL, without port. Raise ValueError for missing hostname, non-HTTP schemes, username/password components, or control characters in the URL. This is syntax validation, not SSRF protection.

## Requirements
- Implement `safe_url_host(url)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Parse URLs with urllib.parse, then validate the scheme and authority.

## Run tests
`python -m pytest tests -q`
