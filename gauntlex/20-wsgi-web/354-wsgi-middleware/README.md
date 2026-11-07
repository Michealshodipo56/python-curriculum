# Wrap an Application

## Description
WSGI middleware surrounds an existing application without replacing its business logic. Add response metadata while forwarding the original body untouched.

## Requirements
- Implement `wrap_app(app)` in `starter/solution.py`.
- Implement `wrap_app(app)` to return a WSGI callable.
- Forward incoming environment and the wrapped application's response behavior.
- Append `X-Powered-By: Gauntlex` exactly once to response headers.
- Do not consume or alter the wrapped application's body iterable.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- Why should middleware return the original iterable rather than reading it eagerly?

## Example Behavior
A wrapped app's original response body remains unchanged, while headers include exactly one `X-Powered-By: Gauntlex`.
