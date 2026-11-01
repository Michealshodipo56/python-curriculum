# Canonical IPv4

## Description
Check whether text is a correctly formed dotted-decimal IPv4 address.

### Behavior contract
Return True only for a canonical dotted-decimal IPv4 address with exactly four components, each decimal 0–255 and no leading zeros unless the component is 0. Reject whitespace and signs.

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Leading zeros, signs, and whitespace can make an address noncanonical.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
