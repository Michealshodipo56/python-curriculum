# redact_secrets

## Description
Replace every case-insensitive occurrence of `password=VALUE` or `token=VALUE` with `password=[REDACTED]` or `token=[REDACTED]`, preserving the original key spelling. VALUE is a nonempty run of non-whitespace characters.

## Requirements
- Implement `redact_secrets(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`redact_secrets("token=abc password=123")` → `"token=[REDACTED] password=[REDACTED]"`

`redact_secrets("TOKEN=x")` → `"TOKEN=[REDACTED]"`

## Tips
Use a regular expression with a captured key and case-insensitive matching.
