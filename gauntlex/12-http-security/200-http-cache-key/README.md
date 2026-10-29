# cache_key

## Challenge
Return a stable SHA-256 lowercase hex digest for a request method, URL and optional body string. Normalize method to uppercase; hash the UTF-8 JSON encoding of the three-element list [method,url,body] using compact separators.

## Requirements
- Implement `cache_key(method, url, body)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
See the contract and write additional edge-case tests.

## Tips
Canonical serialization prevents ambiguous concatenation and makes identical requests hash alike.
