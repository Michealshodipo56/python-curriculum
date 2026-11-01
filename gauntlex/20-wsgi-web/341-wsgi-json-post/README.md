# Validate JSON Input

## Description
Accept structured JSON input and return either a calculated response or a safe client error.

### Behavior contract
Implement POST `/sum` accepting JSON body `{"a":integer,"b":integer}` and returning compact JSON bytes `{"sum":total}` with 200 and Content-Type application/json. Invalid JSON or missing/noninteger values return 400 with body `{"error":"bad request"}`. Other paths return 404.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
In Python, Booleans are a subclass of integers, which matters for validation.

Build the response behavior yourself without a provided implementation.
