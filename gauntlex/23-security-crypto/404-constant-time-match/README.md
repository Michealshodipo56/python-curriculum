# Timing-Resistant Equality

## Description
Compare two UTF-8 strings using a standard-library primitive suitable for sensitive comparisons.

### Behavior contract
Given two UTF-8 strings, return whether they are equal using a constant-time comparison primitive from the standard library. Do not implement a manual early-exit loop.

## Requirements
- Implement `constant_time_match(a, b)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A manual early-exit comparison can reveal information through timing differences.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
