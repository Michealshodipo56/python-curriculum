# Headers Without a Body

## Description
Support GET and HEAD for one resource while respecting their different response-body rules.

### Behavior contract
Implement GET and HEAD `/status`: GET returns bytes `ready`, HEAD returns empty bytes, both with 200 and Content-Type text/plain. All other paths return 404.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
HEAD returns the response metadata without sending the representation body.

Build the response behavior yourself without a provided implementation.
