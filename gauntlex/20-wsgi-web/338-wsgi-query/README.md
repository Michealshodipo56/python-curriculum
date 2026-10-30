# application

## Challenge
Implement GET `/echo` as a WSGI application that reads the first `message` query parameter and returns its UTF-8 bytes. Decode URL form encoding, including plus signs. Other paths return 404. Content-Type text/plain; charset=utf-8.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
parse_qs decodes form query strings.

## Run tests
`python -m pytest tests -q`
