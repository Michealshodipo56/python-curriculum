# Four Network Octets

## Description
Decide whether a string represents a canonical IPv4 address rather than merely resembling one.

### Behavior contract
Return True for a canonical dotted-decimal IPv4 address with exactly four components, each 0–255 and without leading zeros (except '0').

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`valid_ipv4("192.168.0.1")` → `True`

`valid_ipv4("256.1.1.1")` → `False`

## Tips
Validate the number of components, their spelling, and their numeric range independently.

The examples show required behavior, not an implementation.
