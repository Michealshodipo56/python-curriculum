# application

## Challenge
Implement GET `/version` returning ETag `"v1"` and body `version one` with 200. If HTTP_IF_NONE_MATCH exactly equals `"v1"`, return 304 Not Modified with empty body and the same ETag.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Use the Python standard library and the WSGI interface only.
- Never make real network requests in the function tests.
- Return byte strings for WSGI response bodies.
- Do not print debug output or mutate the incoming environment.

## Hint
A conditional request can avoid sending an unchanged representation.

## Run tests
`python -m pytest tests -q`
