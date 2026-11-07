# Allowlisted Query Parameters

## Description

Keep only permitted URL query parameters while preserving their original order and repeated keys.

## Requirements

- Implement `filter_query_params(query, allowed)` in `starter/solution.py`.
- Given a URL query string and an iterable of allowed parameter names, return a compact URL query string containing only allowed parameters in original order, preserving repeated keys. Decode and re-encode form URL encoding. Empty result is empty string.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Treat query parameters as an ordered sequence of key-value pairs so repeated names survive. Decode and re-encode form encoding rather than filtering raw substrings.

## Tips

A mapping may discard repeated query keys; the input is an ordered sequence of pairs.

## Example Behavior

`filter_query_params('a=1&b=2&a=3', ['a'])` → `'a=1&a=3'`.
