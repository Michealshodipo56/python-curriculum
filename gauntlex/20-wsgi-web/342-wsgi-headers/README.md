# Inspect Request Headers

## Description
WSGI represents HTTP request headers through environment keys. Expose a selected header without assuming it exists.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/agent`, read `HTTP_USER_AGENT` from `environ`.
- Return its value as UTF-8 bytes, or empty bytes when absent.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- How do HTTP header names become WSGI environment keys?

## Example Behavior
When `HTTP_USER_AGENT` is `ExampleClient`, the response body is `b'ExampleClient'`.
