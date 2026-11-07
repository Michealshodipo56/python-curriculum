# Record an Action

## Description

Audit records should capture who performed an action, what they did, which resource was involved, and when it occurred. Use caller-supplied facts without inventing new ones.

## Requirements

- Implement `audit_record(actor, action, resource, timestamp)` in `starter/solution.py`.
- Accept `actor`, `action`, `resource`, and `timestamp`.
- Return a dictionary with exactly those four keys and their supplied values.
- Use the caller's timestamp; do not generate the current time.
- Do not modify the supplied values.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

The record contains exactly the supplied four facts. Do not generate a timestamp or add implicit metadata.

## Tips

- Why should the audit function not substitute its own timestamp?

## Example Behavior

`audit_record('ada', 'edit', 'doc-1', '2026-01-01')` → `{'actor': 'ada', 'action': 'edit', 'resource': 'doc-1', 'timestamp': '2026-01-01'}`.
