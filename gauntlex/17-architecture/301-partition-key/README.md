# partition_key

## Challenge
Given a nonempty string identifier and positive partition_count, return the integer index obtained by converting the SHA-256 UTF-8 digest to a big-endian integer and taking modulo partition_count.

## Requirements
- Implement `partition_key(identifier, partition_count)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Stable hashing distributes identifiers without relying on Python's randomized hash.

## Run tests
`python -m pytest tests -q`
