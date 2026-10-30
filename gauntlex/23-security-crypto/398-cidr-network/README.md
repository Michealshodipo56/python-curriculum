# cidr_network

## Challenge
Given an IPv4 CIDR string, return the canonical network address with prefix as `A.B.C.D/N`. Accept host bits in input. Raise ValueError on invalid addresses or prefix lengths.

## Requirements
- Implement `cidr_network(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
ipaddress.ip_network with strict=False canonicalizes host bits.

## Run tests
`python -m pytest tests -q`
