# Record an Action

## Description
Construct a deterministic audit entry from actor, action, resource, and timestamp.

### Behavior contract
Return a dictionary with actor, action, resource, and timestamp keys from the four supplied values. Do not generate the timestamp; it is provided by the caller.

## Requirements
- Implement `audit_record(actor, action, resource, timestamp)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
The timestamp comes from the caller; do not invent one.

Design your own implementation from the specified behavior.
