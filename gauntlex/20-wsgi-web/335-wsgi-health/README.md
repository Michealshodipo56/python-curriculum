# Your First WSGI Response

## Description
WSGI applications receive request metadata and a callback for response headers. Create a health response that works regardless of the requested path.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Call `start_response` exactly once with HTTP 200 and `Content-Type: application/json`.
- Return an iterable containing UTF-8 bytes for `{"status":"ok"}`.
- Do not depend on any particular request path.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
A WSGI application reports status and headers through `start_response`, then returns an iterable of byte chunks. Do not make the health response depend on the path or return a plain string.

## Tips
- Why must the response body contain bytes rather than a Python string?

## Example Behavior
For any request, status is `200 OK` and body is `b'{"status":"ok"}'`.
