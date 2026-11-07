# Timing-Resistant Equality

## Description
Compare two UTF-8 strings using a standard-library primitive suitable for sensitive comparisons.

## Requirements
- Implement `constant_time_match(a, b)` in `starter/solution.py`.
- Given two UTF-8 strings, return whether they are equal using a constant-time comparison primitive from the standard library. Do not implement a manual early-exit loop.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Compare UTF-8 encoded strings with a standard-library timing-resistant equality primitive. Avoid manual loops that stop at the first mismatched byte.

## Tips
A manual early-exit comparison can reveal information through timing differences.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`constant_time_match('café', 'café')` → `True`; `constant_time_match('abc', 'abd')` → `False`.
