# Canonical IPv4

## Description
Check whether text is a correctly formed dotted-decimal IPv4 address.

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Return True only for a canonical dotted-decimal IPv4 address with exactly four components, each decimal 0–255 and no leading zeros unless the component is 0. Reject whitespace and signs.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Validate exactly four ASCII decimal components in canonical dotted notation. Reject whitespace, signs, out-of-range octets, and leading zeros on nonzero-length components.

## Tips
Leading zeros, signs, and whitespace can make an address noncanonical.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`valid_ipv4('192.168.1.1')` → `True`; `valid_ipv4('192.168.01.1')` → `False`.
