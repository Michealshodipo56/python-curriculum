# Time to Live

## Description
Cached data has a limited lifetime. Determine whether an entry remains usable at a given moment, including the exact expiry boundary.

## Requirements
- Implement `cache_valid(created_at, ttl, now)` in `starter/solution.py`.
- Accept creation time, positive time-to-live (`ttl`), and current time.
- Return `True` only while `now` is strictly earlier than `created_at + ttl`.
- Return `False` at or after the expiry instant.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why should an entry expire exactly when its lifetime is exhausted?

## Example Behavior
`cache_valid(100, 30, 129)` → `True`; `cache_valid(100, 30, 130)` → `False`.
