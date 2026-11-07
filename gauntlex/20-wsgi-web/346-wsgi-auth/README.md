# Protect a Private Route

## Description

A private endpoint must verify a bearer credential before releasing its content. Validate the authorization scheme and compare the secret safely.

## Requirements

- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/private`, require Authorization `Bearer secret-token`.
- Treat the `Bearer` scheme case-insensitively.
- Use a timing-resistant comparison for the token.
- Return HTTP 200 with body `welcome` on success, or HTTP 401 with body `unauthorized` otherwise.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.
- Treat a missing `REQUEST_METHOD` environment key as `GET`, as in the supplied callable tests.

## Design Considerations

Validate the authorization scheme separately from the credential and accept case variations of `Bearer`. Compare the supplied token with the expected secret using a timing-resistant operation.

## Tips

- Why should token comparison avoid leaking information through timing differences?

## Example Behavior

`Authorization: bearer secret-token` → HTTP 200; an incorrect token → HTTP 401.
