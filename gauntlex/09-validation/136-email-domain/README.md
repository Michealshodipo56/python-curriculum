# Domain Extraction

## Description
Extract and normalize the domain portion of a valid email address.

### Behavior contract
Given a valid email address with exactly one @, return its domain in lowercase.

## Requirements
- Implement `email_domain(email)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`email_domain("User@Example.COM")` → `"example.com"`

`email_domain("a@sub.example.org")` → `"sub.example.org"`

## Tips
Only the domain needs to be converted to lowercase; do not alter the local part.

The examples specify results without giving an implementation.
