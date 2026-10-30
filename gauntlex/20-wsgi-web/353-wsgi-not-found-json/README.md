# application

## Challenge
Implement a WSGI application that always returns 404 Not Found, Content-Type application/json, and compact JSON bytes `{"error":"not found","path":PATH}` where PATH is PATH_INFO or empty string.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Return a consistent error envelope for unknown routes.

## Run tests
`python -m pytest tests -q`
