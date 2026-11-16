# Worst Service Health

## Description

Implement `health_rollup(statuses)` in `starter/solution.py`. Return `'down'` if any service is down.

## Requirements

- Implement `health_rollup(statuses)` in `starter/solution.py`.
- Accept service statuses `'ok'`, `'degraded'`, and `'down'`.
- Return `'down'` if any service is down.
- Otherwise return `'degraded'` if any service is degraded.
- Return `'ok'` when every service is healthy or the list is empty.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

The summary reflects the most severe status, not the most common one. An empty service list has the defined status `ok`.

## Tips

- **Concept to understand:** A system-wide health summary should reflect its most severe service condition. Combine individual statuses into one result.
- Why should one down service dominate the overall status?

## Example Behavior

`health_rollup(['ok', 'degraded'])` → `'degraded'`; `health_rollup([])` → `'ok'`.
