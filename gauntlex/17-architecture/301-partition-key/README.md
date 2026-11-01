# Choose a Stable Partition

## Description
Map an identifier to one of several partitions in a repeatable way.

### Behavior contract
Given a nonempty string identifier and positive partition_count, return the integer index obtained by converting the SHA-256 UTF-8 digest to a big-endian integer and taking modulo partition_count.

## Requirements
- Implement `partition_key(identifier, partition_count)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Python's built-in hash is not guaranteed to be stable across processes.

Design your own implementation from the specified behavior.
