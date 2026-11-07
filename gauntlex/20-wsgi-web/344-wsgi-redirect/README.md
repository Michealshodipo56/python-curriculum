# Move a Resource

## Description
When a resource moves, a redirect tells clients where to request it next. Preserve distinct behavior for old and new paths.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- GET `/old` returns HTTP 302 Found with `Location: /new` and an empty body.
- GET `/new` returns HTTP 200 and body `new`.
- Other paths return HTTP 404.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
A redirect requires both the redirect status and a `Location` header naming the new path. Keep the destination's ordinary success response separate from the old path.

## Tips
- Why is a Location header needed in addition to a 302 status?

## Example Behavior
GET `/old` → `302 Found`, `Location: /new`, empty body.
