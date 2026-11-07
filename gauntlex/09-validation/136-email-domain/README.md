# Domain Extraction

## Description
An email address has a local part and a domain separated by `@`. Extract the domain and normalize its capitalization without changing the local part.

## Requirements
- Implement `email_domain(email)` in `starter/solution.py`.
- Assume the input is a valid email address containing exactly one `@`.
- Return the substring after `@`.
- Convert the returned domain to lowercase.
- Do not include the separator or local part in the result.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Which part of an email address identifies its domain?
- Why should only the extracted domain be normalized?

## Example Behavior
`email_domain('User@Example.COM')` → `'example.com'`; `email_domain('a@sub.example.org')` → `'sub.example.org'`.
