# Move a Resource

## Description
Return an HTTP redirect from an old path to a new one.

### Behavior contract
Implement a WSGI application redirecting GET `/old` to `/new` using 302 Found and a Location header; response body empty. GET `/new` returns 200 with body `new`. Other paths return 404.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
A redirect needs both a 3xx status and a Location header.

Build the response behavior yourself without a provided implementation.
