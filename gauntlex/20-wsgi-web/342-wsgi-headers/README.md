# Inspect Request Headers

## Description
Read an HTTP request header from its WSGI environment representation.

### Behavior contract
Implement GET `/agent` returning the HTTP_USER_AGENT environment value as UTF-8 bytes, or empty bytes if absent, with 200 and Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
HTTP header names are mapped to specially prefixed environment keys.

Build the response behavior yourself without a provided implementation.
