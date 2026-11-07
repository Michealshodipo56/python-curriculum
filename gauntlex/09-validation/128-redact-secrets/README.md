# Hide Sensitive Tokens

## Description
Hide credential values in text while preserving the original capitalization of their keys. Only explicitly recognized assignment forms should be changed.

## Requirements
- Implement `redact_secrets(text)` in `starter/solution.py`.
- Find case-insensitive occurrences of `password=VALUE` or `token=VALUE`.
- Treat `VALUE` as a nonempty consecutive run of nonwhitespace characters.
- Replace each matched value with `[REDACTED]`.
- Preserve the original spelling and capitalization of each key and all unmatched text.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should the key's original spelling remain unchanged?
- How do spaces and punctuation affect the end of a credential value?

## Example Behavior
`redact_secrets('token=abc password=123')` → `'token=[REDACTED] password=[REDACTED]'`; `redact_secrets('TOKEN=x')` → `'TOKEN=[REDACTED]'`.
