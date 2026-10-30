# application

## Challenge
Implement GET `/public` returning 200 body `ok` and Access-Control-Allow-Origin `https://gauntlex.example` only when HTTP_ORIGIN exactly equals that origin. For any other origin, omit the header. Return Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
An origin allowlist must compare full origins exactly.

## Run tests
`python -m pytest tests -q`
