# Route by Path

## Description
Choose an HTTP response according to the path supplied in the WSGI environment.

### Behavior contract
Implement a WSGI callable routing PATH_INFO `/health` to 200 with body `ok`, and all other paths to 404 with body `not found`. Return Content-Type text/plain; charset=utf-8.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Unknown paths should not accidentally receive the success response.

Build the response behavior yourself without a provided implementation.
