# Time to Live

## Description
Decide whether a cached value is still valid at a particular time.

### Behavior contract
Return True if an item created at timestamp created_at with positive ttl is still valid at now. Validity is now < created_at+ttl.

## Requirements
- Implement `cache_valid(created_at, ttl, now)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
The exact expiry instant is no longer valid.

Design your own implementation from the specified behavior.
