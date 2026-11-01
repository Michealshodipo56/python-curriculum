# Safe Server Errors

## Description
Convert an internal failure into a predictable response without exposing exception details.

### Behavior contract
Implement GET `/safe` returning 200 and body `ok`; GET `/crash` must catch an internal ValueError and return 500 with body `internal error`, without exposing exception details. Return Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
An error message intended for a developer is not necessarily safe for an API client.

Build the response behavior yourself without a provided implementation.
