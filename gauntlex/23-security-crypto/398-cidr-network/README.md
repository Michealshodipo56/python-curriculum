# Normalize a Network

## Description
Turn an IPv4 CIDR expression into its canonical network address and prefix.

## Requirements
- Implement `cidr_network(text)` in `starter/solution.py`.
- Given an IPv4 CIDR string, return the canonical network address with prefix as `A.B.C.D/N`. Accept host bits in input. Raise ValueError on invalid addresses or prefix lengths.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Parse the IPv4 address and prefix with standard-library networking utilities, accepting host bits in the input while returning the canonical network address.

## Tips
Host bits may be present in the input, but the result represents the network.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`cidr_network('192.168.1.42/24')` → `'192.168.1.0/24'`.
