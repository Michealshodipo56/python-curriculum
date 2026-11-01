# Replay Exactly Once

## Description
Reconstruct balances from events while applying each event identifier at most once.

### Behavior contract
Given a list of event dictionaries with unique string id and account/delta fields, return account balances while applying each event ID at most once (first occurrence wins).

## Requirements
- Implement `replay_unique(events)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Deduplication must happen before applying an event's effect.

Design your own implementation from the specified behavior.
