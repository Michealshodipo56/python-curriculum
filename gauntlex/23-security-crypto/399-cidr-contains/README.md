# Network Membership

## Description

Determine whether an IPv4 address belongs to a specified CIDR network.

## Requirements

- Implement `cidr_contains(network, address)` in `starter/solution.py`.
- Return True if IPv4 address belongs to IPv4 CIDR network, otherwise False. Raise ValueError on malformed inputs.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Determine membership from the full IPv4 network prefix rather than textual address prefixes. Malformed network or address inputs must raise `ValueError`.

## Tips

Network membership depends on the prefix length, not just matching leading text.

## Example Behavior

`cidr_contains('10.0.0.0/8', '10.2.3.4')` → `True`; `cidr_contains('10.0.0.0/8', '11.0.0.1')` → `False`.
