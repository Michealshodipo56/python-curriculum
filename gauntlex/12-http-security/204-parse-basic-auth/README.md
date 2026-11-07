# Decode Basic Credentials

## Description

HTTP Basic authorization carries a Base64-encoded username and password separated by a colon. Decode the credentials and reject malformed input without exposing secrets.

## Requirements

- Implement `parse_basic_auth(header)` in `starter/solution.py`.
- Accept an Authorization header using the `Basic` scheme followed by a Base64 payload.
- Decode valid Base64 data as UTF-8.
- Split the decoded credentials at the first colon into username and password; allow additional colons inside the password.
- Return `[username, password]` for valid input.
- Return `None` for an invalid scheme, Base64 payload, UTF-8 sequence, or missing colon.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips

- Why must the first colon be the separator?
- Why does Base64 encoding not provide encryption?

## Example Behavior

`parse_basic_auth("Basic YWRhOnNlY3JldA==")` → `["ada", "secret"]`

`parse_basic_auth("Bearer x")` → `None`
