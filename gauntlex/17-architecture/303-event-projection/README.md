# project_balances

## Challenge
Given a list of event dictionaries with account string, delta integer, and unique id string, return a mapping of account to final integer balance, summing deltas in event order. Accounts with net zero remain present.

## Requirements
- Implement `project_balances(events)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
A projection reduces an event stream into current state.

## Run tests
`python -m pytest tests -q`
