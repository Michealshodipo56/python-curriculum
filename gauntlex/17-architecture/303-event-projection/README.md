# Rebuild Account Balances

## Description

Event-sourced state can be rebuilt by applying recorded changes. Derive each account's current balance from its event deltas.

## Requirements

- Implement `project_balances(events)` in `starter/solution.py`.
- Accept events containing `id`, string `account`, and integer `delta` fields; IDs are unique.
- Accumulate deltas for each account in event order, beginning from zero.
- Return a dictionary from account names to integer balances.
- Keep accounts whose net balance is zero in the result.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

A zero net balance is still a meaningful account result. Events are applied in their supplied order without requiring a database.

## Tips

- Why should an account remain present when its total returns to zero?

## Example Behavior

`project_balances([{'id': '1', 'account': 'a', 'delta': 3}, {'id': '2', 'account': 'a', 'delta': -3}])` → `{'a': 0}`.
