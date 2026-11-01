# Normalize a Network

## Description
Turn an IPv4 CIDR expression into its canonical network address and prefix.

### Behavior contract
Given an IPv4 CIDR string, return the canonical network address with prefix as `A.B.C.D/N`. Accept host bits in input. Raise ValueError on invalid addresses or prefix lengths.

## Requirements
- Implement `cidr_network(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Host bits may be present in the input, but the result represents the network.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
