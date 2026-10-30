# application

## Challenge
Implement GET and HEAD `/status`: GET returns bytes `ready`, HEAD returns empty bytes, both with 200 and Content-Type text/plain. All other paths return 404.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
HEAD has headers but no response body.

## Run tests
`python -m pytest tests -q`
