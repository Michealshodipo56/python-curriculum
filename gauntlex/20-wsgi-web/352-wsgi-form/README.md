# Read Form Fields

## Description
Decode a URL-encoded POST body and return a selected form value.

### Behavior contract
Implement POST `/form` accepting application/x-www-form-urlencoded body and returning the first `name` value as UTF-8 bytes, or empty bytes if absent. Return 200 with Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Form data uses percent decoding and plus-as-space rules.

Build the response behavior yourself without a provided implementation.
