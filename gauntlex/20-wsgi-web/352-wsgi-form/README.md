# application

## Challenge
Implement POST `/form` accepting application/x-www-form-urlencoded body and returning the first `name` value as UTF-8 bytes, or empty bytes if absent. Return 200 with Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Form bodies use the same encoding rules as URL query strings.

## Run tests
`python -m pytest tests -q`
