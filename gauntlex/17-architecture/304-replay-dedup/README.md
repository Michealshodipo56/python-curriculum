# Replay Exactly Once

## Description
Repeated delivery must not apply the same account event more than once. Rebuild balances while treating each event ID as unique.

## Requirements
- Implement `replay_unique(events)` in `starter/solution.py`.
- Accept events with string `id`, account, and integer delta fields.
- Apply only the first occurrence of each event ID.
- Sum retained deltas by account, starting from zero.
- Return final balances, including accounts with zero totals.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why must deduplication happen before updating balances?

## Example Behavior
Two deliveries of `{'id': 'x', 'account': 'a', 'delta': 5}` produce balance `{'a': 5}`, not `{'a': 10}`.
