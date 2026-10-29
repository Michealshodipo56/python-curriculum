# eviction_candidates

## Challenge
Given mapping key->last_access integer and a nonnegative maximum count to keep, return keys to evict ordered by oldest access first and then alphabetically. Evict only enough to reach maximum count.

## Requirements
- Implement `eviction_candidates(accesses, max_items)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Sort by access time and key to resolve ties.

## Run tests
`python -m pytest tests -q`
