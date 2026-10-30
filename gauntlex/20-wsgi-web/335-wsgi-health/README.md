# application

## Challenge
Implement a WSGI callable returning HTTP 200, Content-Type application/json, and UTF-8 bytes `{"status":"ok"}` for any request. Call start_response exactly once.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
A WSGI application returns an iterable of byte strings.

## Run tests
`python -m pytest tests -q`
