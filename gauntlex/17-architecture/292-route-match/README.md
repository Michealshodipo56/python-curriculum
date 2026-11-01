# Capture Route Parameters

## Description
Match a request path to a template containing literal and variable segments.

### Behavior contract
Match an HTTP path to a route template with literal segments and parameters written `{name}`. Return a dict of captured parameter values, or None on mismatch. Paths must have matching segment counts. Do not decode percent escapes.

## Requirements
- Implement `match_route(template, path)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Literal segments must match exactly; parameter segments capture values.

Design your own implementation from the specified behavior.
