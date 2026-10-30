# application

## Challenge
Implement a WSGI callable accepting GET `/resource` with 200 body `resource`, rejecting other methods for that path with 405 body `method not allowed`, and returning 404 body `not found` for other paths. Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Check the route and allowed method separately.

## Run tests
`python -m pytest tests -q`
