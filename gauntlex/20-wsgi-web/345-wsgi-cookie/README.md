# Recognize a Session Cookie

## Description
Read a Cookie header and determine whether it contains a meaningful session value.

### Behavior contract
Implement GET `/cookie` returning body `seen` if HTTP_COOKIE contains a cookie named session with a nonempty value, otherwise `missing`. Return 200 and Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
A cookie's presence is not enough when its value is empty.

Build the response behavior yourself without a provided implementation.
