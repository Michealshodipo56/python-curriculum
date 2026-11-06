# Choose a Stable Partition

## Description
Distributed storage often assigns records to partitions using a repeatable hash. The same identifier must map to the same partition across processes.

## Requirements
- Implement `partition_key(identifier, partition_count)` in `starter/solution.py`.
- Accept a nonempty identifier string and a positive partition count.
- Hash the identifier's UTF-8 bytes with SHA-256.
- Interpret the digest as one unsigned big-endian integer.
- Return that integer modulo the partition count.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why is Python's built-in hash unsuitable for stable cross-process partitioning?

## Example Behavior
For any valid input, the returned partition is an integer from `0` through `partition_count - 1`.
