# deduplicate_events

## Challenge
Given a list of event dictionaries with string id fields, return first occurrences of each id in original order as shallow copies. Do not mutate inputs.

## Requirements
- Implement `deduplicate_events(events)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Use a seen-ID set to make deduplication linear.

## Run tests
`python -m pytest tests -q`
