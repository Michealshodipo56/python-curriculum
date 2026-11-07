# Route by Path

## Description
A web service chooses responses using the request path. Distinguish a known health route from all other locations.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Read `PATH_INFO` from the WSGI environment.
- For `/health`, return HTTP 200 with body `ok`.
- For other paths, return HTTP 404 with body `not found`.
- Use `Content-Type: text/plain; charset=utf-8`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Choose status and body from `PATH_INFO` before starting the response. Keep the health route distinct from every unknown path so missing resources never receive a success status.

## Tips
- Why should an unknown route not share the health route's success status?

## Example Behavior
`/health` → `200` and `b'ok'`; `/missing` → `404` and `b'not found'`.
