# Headers Without a Body

## Description
GET retrieves a resource body, while HEAD requests only response metadata. Support both on one route.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/status`, return HTTP 200 and body `ready`.
- For HEAD `/status`, return HTTP 200 and an empty body.
- Use `Content-Type: text/plain` for both.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Preserve the route's successful status and response metadata for HEAD while omitting its body. GET and HEAD differ in representation delivery, not in whether the resource exists.

## Tips
- Why does HEAD omit a body even when the resource exists?

## Example Behavior
GET `/status` → `b'ready'`; HEAD `/status` → `b''`.
