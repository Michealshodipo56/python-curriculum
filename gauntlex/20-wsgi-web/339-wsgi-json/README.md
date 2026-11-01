# Serialize a Web Response

## Description
Return a stable JSON representation with the correct content type.

### Behavior contract
Implement GET `/data` returning compact sorted-key JSON bytes of `{"name":"Gauntlex","ready":true}` with Content-Type application/json and 200 status. Other paths return 404 and empty bytes.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
JSON Boolean spelling differs from Python Boolean spelling.

Build the response behavior yourself without a provided implementation.
