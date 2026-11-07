# Inspect a Web Host

## Description

Extract a valid HTTP or HTTPS hostname while rejecting malformed authorities and unsafe URL syntax.

## Requirements

- Implement `safe_url_host(url)` in `starter/solution.py`.
- Return lowercase hostname from an absolute HTTP or HTTPS URL, without port. Raise ValueError for missing hostname, non-HTTP schemes, username/password components, or control characters in the URL. This is syntax validation, not SSRF protection.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Validate URL scheme, authority, credentials, and control characters before returning a normalized hostname. Hostname extraction alone is not sufficient protection against SSRF.

## Tips

Syntax validation alone does not make a URL safe to fetch; SSRF defenses require additional checks.

## Example Behavior

`safe_url_host('https://Example.COM:443/path')` → `'example.com'`; a URL containing user credentials raises `ValueError`.
