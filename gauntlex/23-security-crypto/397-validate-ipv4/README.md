# valid_ipv4

## Challenge
Return True only for a canonical dotted-decimal IPv4 address with exactly four components, each decimal 0–255 and no leading zeros unless the component is 0. Reject whitespace and signs.

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Check component syntax before integer range.

## Run tests
`python -m pytest tests -q`
