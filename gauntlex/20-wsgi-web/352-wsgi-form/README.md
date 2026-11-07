# Read Form Fields

## Description
HTML forms commonly submit URL-encoded data in a POST body. Decode it and extract the first matching field.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/form`, read the `application/x-www-form-urlencoded` body.
- Decode percent escapes and plus-as-space encoding.
- Return the first `name` field value as UTF-8 bytes, or empty bytes if absent.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Tips
- Why should repeated form fields use the first value for this contract?

## Example Behavior
POST body `name=Ada+Lovelace` → `b'Ada Lovelace'`.
