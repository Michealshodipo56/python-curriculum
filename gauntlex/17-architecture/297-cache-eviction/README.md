# Evict the Oldest

## Description
A bounded cache must discard entries when its capacity is exceeded. Prefer the least recently accessed entries and break ties consistently.

## Requirements
- Implement `eviction_candidates(accesses, max_items)` in `starter/solution.py`.
- Accept a mapping from cache keys to integer last-access timestamps and a nonnegative maximum item count.
- Return only enough keys to reduce the cache to that maximum.
- Order eviction candidates by oldest access time, then alphabetically by key.
- Return `[]` when the cache is already within capacity.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why must tied access times use a secondary sort order?

## Example Behavior
With `{'b': 1, 'a': 1, 'c': 3}` and a limit of 1, evict `['a', 'b']`.
