# Allowlisted Query Parameters

## Description
Keep only permitted URL query parameters while preserving their original order and repeated keys.

### Behavior contract
Given a URL query string and an iterable of allowed parameter names, return a compact URL query string containing only allowed parameters in original order, preserving repeated keys. Decode and re-encode form URL encoding. Empty result is empty string.

## Requirements
- Implement `filter_query_params(query, allowed)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
A mapping may discard repeated query keys; the input is an ordered sequence of pairs.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
