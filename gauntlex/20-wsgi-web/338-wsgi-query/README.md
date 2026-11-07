# Decode Query Input

## Description
Query parameters are encoded separately from the URL path. Decode the first `message` value on an echo route.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Handle GET `/echo` and read the first `message` value from `QUERY_STRING`.
- Decode percent escapes and plus-as-space form encoding.
- Return the decoded message as UTF-8 bytes and use text/plain with UTF-8 charset.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- Why is splitting a raw query string on every equals sign unreliable?

## Example Behavior
GET `/echo?message=hello+world` → `b'hello world'`.
