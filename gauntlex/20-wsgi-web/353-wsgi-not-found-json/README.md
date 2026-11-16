# Consistent Not Found

## Description

Implement `application(environ, start_response)` in `starter/solution.py`. Return HTTP 404 Not Found for every request.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- Return HTTP 404 Not Found for every request.
- Set `Content-Type: application/json`.
- Return compact JSON with keys `error` set to `not found` and `path` set to `PATH_INFO` or `''` when missing.
- Return JSON as bytes.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations

Serialize the error and requested path as a compact JSON object and encode it to bytes. Even a service that always returns 404 must send consistent content type and response status.

## Tips

- **Concept to understand:** Even an error-only service should provide predictable JSON and HTTP metadata. Include the requested path in a structured not-found response.
- Why does a structured error need the same encoding discipline as a successful response?

## Example Behavior

With `PATH_INFO='/missing'`, body is `b'{"error":"not found","path":"/missing"}'`.
