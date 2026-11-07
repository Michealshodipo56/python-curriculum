# Four Network Octets

## Description

An IPv4 address has four dotted decimal components, but not every four-part numeric string is valid. Validate both the structure and canonical spelling.

## Requirements

- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Return `True` only for exactly four dot-separated decimal components.
- Each component must contain ASCII digits and represent a number from `0` through `255`.
- Reject leading zeros except when a component is exactly `0`.
- Reject whitespace, signs, missing components, and extra components.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why are numeric range checks alone insufficient?
- What distinguishes `0` from `00` in canonical notation?

## Example Behavior

`valid_ipv4('192.168.0.1')` → `True`; `valid_ipv4('256.1.1.1')` → `False`.
