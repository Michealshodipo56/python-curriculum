# Validate Request IDs

## Description
Accept a supplied request identifier only when it satisfies a strict format.

### Behavior contract
Implement GET `/request` returning 200 and body `ok`, with X-Request-ID header equal to HTTP_X_REQUEST_ID if it is a nonempty ASCII alphanumeric string of at most 32 characters. Otherwise use `generated`.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Never reflect arbitrary header text into a response without validation.

Build the response behavior yourself without a provided implementation.
