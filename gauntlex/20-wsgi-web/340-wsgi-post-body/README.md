# Read a Request Body

## Description
Read a declared number of request bytes and transform the decoded text.

### Behavior contract
Implement POST `/uppercase` reading exactly CONTENT_LENGTH bytes from `wsgi.input`, decoding UTF-8, uppercasing text, and returning UTF-8 bytes with 200 status. Other paths return 404. Content-Type text/plain.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Tips
Never read beyond the advertised content length.

Build the response behavior yourself without a provided implementation.
