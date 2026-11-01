# Network Membership

## Description
Determine whether an IPv4 address belongs to a specified CIDR network.

### Behavior contract
Return True if IPv4 address belongs to IPv4 CIDR network, otherwise False. Raise ValueError on malformed inputs.

## Requirements
- Implement `cidr_contains(network, address)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Network membership depends on the prefix length, not just matching leading text.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
