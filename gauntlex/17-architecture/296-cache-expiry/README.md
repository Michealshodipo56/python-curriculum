# cache_valid

## Challenge
Return True if an item created at timestamp created_at with positive ttl is still valid at now. Validity is now < created_at+ttl.

## Requirements
- Implement `cache_valid(created_at, ttl, now)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
The expiry boundary is exclusive.

## Run tests
`python -m pytest tests -q`
