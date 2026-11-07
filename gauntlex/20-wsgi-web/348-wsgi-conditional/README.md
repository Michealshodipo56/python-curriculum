# Avoid Unchanged Responses

## Description
Entity tags allow a client to ask whether cached content is still current. Return a body only when the tag does not match.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/version`, set `ETag` to the exact value `"v1"`.
- Without an exact matching `HTTP_IF_NONE_MATCH`, return HTTP 200 with body `version one`.
- With an exact match, return HTTP 304 Not Modified and an empty body.
- Include the same ETag in both responses.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- Why should a 304 response omit the representation body?

## Example Behavior
`If-None-Match: "v1"` → HTTP 304 with empty body and ETag `"v1"`.
