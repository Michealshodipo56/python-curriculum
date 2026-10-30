# application

## Challenge
Implement GET `/request` returning 200 and body `ok`, with X-Request-ID header equal to HTTP_X_REQUEST_ID if it is a nonempty ASCII alphanumeric string of at most 32 characters. Otherwise use `generated`.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Validate untrusted header values before reflecting them.

## Run tests
`python -m pytest tests -q`
