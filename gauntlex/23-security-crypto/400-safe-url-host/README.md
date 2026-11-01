# Inspect a Web Host

## Description
Extract a valid HTTP or HTTPS hostname while rejecting malformed authorities and unsafe URL syntax.

### Behavior contract
Return lowercase hostname from an absolute HTTP or HTTPS URL, without port. Raise ValueError for missing hostname, non-HTTP schemes, username/password components, or control characters in the URL. This is syntax validation, not SSRF protection.

## Requirements
- Implement `safe_url_host(url)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Syntax validation alone does not make a URL safe to fetch; SSRF defenses require additional checks.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
