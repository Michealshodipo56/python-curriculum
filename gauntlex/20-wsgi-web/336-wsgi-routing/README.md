# application

## Challenge
Implement a WSGI callable routing PATH_INFO `/health` to 200 with body `ok`, and all other paths to 404 with body `not found`. Return Content-Type text/plain; charset=utf-8.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Dispatch by the path field in the WSGI environment.

## Run tests
`python -m pytest tests -q`
