# Hide Sensitive Headers

## Description

Create a copy of HTTP headers with credential-bearing values redacted.

## Requirements

- Implement `redact_headers(headers)` in `starter/solution.py`.
- Given a mapping of HTTP header names to strings, return a new mapping with values replaced by `[REDACTED]` for Authorization, Cookie, Set-Cookie and X-API-Key, case-insensitively. Preserve original key casing and other values.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Match sensitive header names case-insensitively but preserve the caller's original header spelling in the copied result. Never modify the source mapping.

## Tips

Preserve original header names while comparing them without regard to case.

## Example Behavior

`redact_headers({'authorization': 'Bearer abc', 'Accept': 'text/plain'})` → `{'authorization': '[REDACTED]', 'Accept': 'text/plain'}`.
