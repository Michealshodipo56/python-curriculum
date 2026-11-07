# Count Response Bytes

## Description
HTTP Content-Length measures bytes rather than Unicode characters. Build a response containing a non-ASCII character and report its encoded size.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/payload`, return UTF-8 bytes for `café` with HTTP 200.
- Set `Content-Type: text/plain; charset=utf-8`.
- Set `Content-Length` to the decimal byte length of the actual response body.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Encode the response body to UTF-8 before measuring its size. `Content-Length` describes transmitted bytes, not Unicode code points or the length of a source string.

## Tips
- Why is the length of a Unicode string not always its UTF-8 byte length?

## Example Behavior
GET `/payload` → body `b'caf\xc3\xa9'` and `Content-Length: 5`.
