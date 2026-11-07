# Method Matters

## Description

The same URL can support one HTTP method while rejecting another. Distinguish a missing route from a disallowed method.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- Accept GET `/resource` with HTTP 200 and body `resource`.
- Return HTTP 405 with body `method not allowed` for other methods at `/resource`.
- Return HTTP 404 with body `not found` for other paths.
- Set a text/plain content type.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations

Check route existence and request method separately: a known resource with an unsupported method is not the same as an unknown URL. Keep each status paired with its specified body.

## Tips

- What information does 405 convey that 404 does not?

## Example Behavior

GET `/resource` → `200`; POST `/resource` → `405`; GET `/else` → `404`.
