# Decode Basic Credentials

## Description
Interpret a Basic authorization header and recover a username and password from its encoded payload.

### Behavior contract
Parse `Basic BASE64` Authorization and return [username,password]. Decode UTF-8 and split credentials at the first colon. Return None for invalid scheme, Base64, UTF-8, or missing colon.

## Requirements
- Implement `parse_basic_auth(header)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`parse_basic_auth("Basic YWRhOnNlY3JldA==")` → `["ada", "secret"]`

`parse_basic_auth("Bearer x")` → `None`

## Tips
The first colon separates username from password; later colons can belong to the password.

Examples describe the contract, not a solution.
