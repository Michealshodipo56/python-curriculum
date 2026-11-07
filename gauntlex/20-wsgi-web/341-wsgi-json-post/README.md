# Validate JSON Input

## Description
A JSON endpoint must validate structure and field types before computing a result. Invalid input should produce a stable client error.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/sum`, accept JSON containing integer `a` and integer `b`.
- Return compact JSON `{"sum":total}` with HTTP 200.
- For malformed JSON or missing/noninteger fields, return HTTP 400 and `{"error":"bad request"}`.
- Use `Content-Type: application/json`; return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- Why must Boolean values be considered separately when validating Python integers?

## Example Behavior
POST `/sum` with `{"a":2,"b":3}` → `b'{"sum":5}'`; invalid input → HTTP 400.
