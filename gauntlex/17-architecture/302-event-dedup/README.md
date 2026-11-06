# Keep First Events

## Description
An event stream may contain duplicate deliveries. Keep the first occurrence of each event ID and preserve event order.

## Requirements
- Implement `deduplicate_events(events)` in `starter/solution.py`.
- Accept event dictionaries with string `id` fields.
- Return the first event for each distinct ID in original order.
- Return shallow copies of retained event dictionaries.
- Do not mutate the original events or allow later duplicates to overwrite earlier ones.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Tips
- Why should the first occurrence win rather than the last?

## Example Behavior
Events with IDs `a`, `b`, `a` produce two retained events, ordered `a`, `b`.
