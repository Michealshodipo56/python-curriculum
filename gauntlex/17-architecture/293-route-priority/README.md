# route_priority

## Challenge
Return the number of literal segments in a route template. A segment is dynamic only if it starts with { and ends with }. Ignore empty segments caused by leading or trailing slashes.

## Requirements
- Implement `route_priority(template)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Literal segments make a route more specific.

## Run tests
`python -m pytest tests -q`
