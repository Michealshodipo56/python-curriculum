# Wrap an Application

## Description
Add one response header around an existing WSGI application without changing its behavior.

### Behavior contract
Implement a WSGI middleware factory taking an application callable and returning a WSGI application that forwards requests and responses unchanged except for appending header `X-Powered-By: Gauntlex` exactly once. Do not consume or alter the body iterable.

## Requirements
- Implement `wrap_app(app)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Middleware should forward the original body iterable rather than consuming it.

Build the response behavior yourself without a provided implementation.
