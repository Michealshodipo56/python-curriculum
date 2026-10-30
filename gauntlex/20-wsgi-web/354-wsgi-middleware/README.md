# wrap_app

## Challenge
Implement a WSGI middleware factory taking an application callable and returning a WSGI application that forwards requests and responses unchanged except for appending header `X-Powered-By: Gauntlex` exactly once. Do not consume or alter the body iterable.

## Requirements
- Implement `wrap_app(app)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
Wrap start_response while passing the original response iterable through.

## Run tests
`python -m pytest tests -q`
