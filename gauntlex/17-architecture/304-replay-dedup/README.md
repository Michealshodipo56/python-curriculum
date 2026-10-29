# replay_unique

## Challenge
Given a list of event dictionaries with unique string id and account/delta fields, return account balances while applying each event ID at most once (first occurrence wins).

## Requirements
- Implement `replay_unique(events)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Deduplicate before applying events to keep replay idempotent.

## Run tests
`python -m pytest tests -q`
