# Evict the Oldest

## Description
Choose which cache entries to remove when the cache exceeds its allowed size.

### Behavior contract
Given mapping key->last_access integer and a nonnegative maximum count to keep, return keys to evict ordered by oldest access first and then alphabetically. Evict only enough to reach maximum count.

## Requirements
- Implement `eviction_candidates(accesses, max_items)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
When access times tie, use the specified secondary ordering.

Design your own implementation from the specified behavior.
