# Read a Request Body

## Description

WSGI exposes request bodies as a byte stream. Read only the declared bytes before transforming their decoded text.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/uppercase`, read exactly `CONTENT_LENGTH` bytes from `wsgi.input`.
- Decode UTF-8, uppercase the text, and return UTF-8 bytes with HTTP 200.
- Set `Content-Type: text/plain`.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations

Respect the declared request-body byte count when reading `wsgi.input`. Decode only the bytes belonging to this request and keep the response body in bytes after transforming text.

## Tips

- What could go wrong if the application reads beyond the advertised length?

## Example Behavior

POST `/uppercase` with body `hello` → `b'HELLO'`.
