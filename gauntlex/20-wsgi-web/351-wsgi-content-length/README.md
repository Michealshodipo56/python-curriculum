# application

## Challenge
Implement GET `/payload` returning 200 with UTF-8 bytes for `café`, Content-Type text/plain; charset=utf-8, and Content-Length set to the byte length of the response body.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Byte length differs from character length for non-ASCII text.

## Run tests
`python -m pytest tests -q`
