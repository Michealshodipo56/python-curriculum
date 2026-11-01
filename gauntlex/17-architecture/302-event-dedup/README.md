# Keep First Events

## Description
Remove duplicate events by identifier while preserving first appearance.

### Behavior contract
Given a list of event dictionaries with string id fields, return first occurrences of each id in original order as shallow copies. Do not mutate inputs.

## Requirements
- Implement `deduplicate_events(events)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
An event with a repeated ID must not overwrite the first accepted event.

Design your own implementation from the specified behavior.
