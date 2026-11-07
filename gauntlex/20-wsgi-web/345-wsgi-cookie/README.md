# Recognize a Session Cookie

## Description

Cookies arrive in a request header containing multiple name-value pairs. Determine whether a meaningful session cookie exists.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/cookie`, inspect `HTTP_COOKIE`.
- Return body `seen` when a cookie named `session` has a nonempty value.
- Otherwise return body `missing`.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.
- Treat a missing `REQUEST_METHOD` environment key as `GET`, as in the supplied callable tests.

## Design Considerations

Parse cookie name-value pairs without mistaking the mere presence of `session` for a usable session. The contract requires a nonempty value; other cookie names must not affect the result.

## Tips

- Why is the presence of a cookie name insufficient when its value is empty?

## Example Behavior

`HTTP_COOKIE='theme=dark; session=abc'` → `b'seen'`; `session=` → `b'missing'`.
