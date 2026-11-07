# Serialize a Web Response

## Description
A JSON API must serialize Python data into valid compact JSON and label its response correctly.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/data`, return HTTP 200 and `Content-Type: application/json`.
- Serialize `{"name":"Gauntlex","ready":true}` as compact JSON with sorted keys.
- Return the encoded bytes.
- For other paths, return HTTP 404 with an empty body.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Construct a JSON representation rather than Python's string representation of a dictionary. Serialize deterministically with compact separators and sorted keys, then encode it to bytes.

## Tips
- Why is Python's `True` not the same literal as JSON's `true`?

## Example Behavior
GET `/data` → `b'{"name":"Gauntlex","ready":true}'`.
