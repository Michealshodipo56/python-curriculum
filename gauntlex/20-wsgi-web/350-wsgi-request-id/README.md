# Validate Request IDs

## Description
Request identifiers can help correlate logs, but arbitrary client-supplied header values should not be reflected without validation.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/request`, return HTTP 200 with body `ok`.
- Accept `HTTP_X_REQUEST_ID` only when it is nonempty ASCII alphanumeric text of at most 32 characters.
- Set `X-Request-ID` to that accepted value, or to `generated` otherwise.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Validate both ASCII-only alphanumeric characters and the maximum length before reflecting a client-provided identifier. Use the prescribed fallback when any check fails.

## Tips
- Why must length and character restrictions be checked before reflecting a header?

## Example Behavior
`HTTP_X_REQUEST_ID='abc123'` → response header `X-Request-ID: abc123`; `abc-123` → `generated`.
