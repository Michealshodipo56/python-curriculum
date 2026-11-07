# Control Cross-Origin Access

## Description

Cross-origin headers must not trust origins merely because they resemble an approved domain. Allow only one exact origin.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/public`, return HTTP 200 and body `ok`.
- Add `Access-Control-Allow-Origin: https://gauntlex.example` only when `HTTP_ORIGIN` exactly matches that value.
- Omit the allow-origin header for missing or different origins.
- Set `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.
- Treat a missing `REQUEST_METHOD` environment key as `GET`, as in the supplied callable tests.

## Design Considerations

Treat the approved origin as an exact string, not a suffix or substring pattern. Omit the allow-origin header entirely for missing or unapproved origins rather than reflecting untrusted input.

## Tips

- Why is a suffix or substring match unsafe for origin allowlists?

## Example Behavior

Origin `https://gauntlex.example` receives the allow-origin header; `https://gauntlex.example.evil` does not.
