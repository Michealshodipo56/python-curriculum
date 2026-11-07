# Safe Server Errors

## Description

An internal exception should not expose implementation details to API clients. Provide a predictable failure response while preserving normal behavior.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- GET `/safe` returns HTTP 200 with body `ok`.
- GET `/crash` catches an internal `ValueError` and returns HTTP 500 with body `internal error`.
- Do not expose exception text in the response.
- Use `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.
- Treat a missing `REQUEST_METHOD` environment key as `GET`, as in the supplied callable tests.

## Design Considerations

Convert the expected internal failure into a stable HTTP 500 response without exposing exception details or a traceback. Keep the ordinary route's successful response unaffected.

## Tips

- Why is a developer-facing exception message unsafe to return directly?

## Example Behavior

GET `/crash` → HTTP 500 with `b'internal error'`, not a traceback.
