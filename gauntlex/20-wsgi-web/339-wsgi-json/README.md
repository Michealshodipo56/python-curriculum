# application

## Challenge
Implement GET `/data` returning compact sorted-key JSON bytes of `{"name":"Gauntlex","ready":true}` with Content-Type application/json and 200 status. Other paths return 404 and empty bytes.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
JSON booleans are lowercase in serialized output.

## Run tests
`python -m pytest tests -q`
