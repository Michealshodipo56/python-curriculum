# audit_record

## Challenge
Return a dictionary with actor, action, resource, and timestamp keys from the four supplied values. Do not generate the timestamp; it is provided by the caller.

## Requirements
- Implement `audit_record(actor, action, resource, timestamp)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Keep audit data explicit and deterministic.

## Run tests
`python -m pytest tests -q`
