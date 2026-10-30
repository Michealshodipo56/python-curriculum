# cidr_contains

## Challenge
Return True if IPv4 address belongs to IPv4 CIDR network, otherwise False. Raise ValueError on malformed inputs.

## Requirements
- Implement `cidr_contains(network, address)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Use standard library ipaddress membership.

## Run tests
`python -m pytest tests -q`
