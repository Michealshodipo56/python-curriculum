# application

## Challenge
Implement GET `/cookie` returning body `seen` if HTTP_COOKIE contains a cookie named session with a nonempty value, otherwise `missing`. Return 200 and Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Cookie pairs are separated by semicolons.

## Run tests
`python -m pytest tests -q`
