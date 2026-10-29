# match_route

## Challenge
Match an HTTP path to a route template with literal segments and parameters written `{name}`. Return a dict of captured parameter values, or None on mismatch. Paths must have matching segment counts. Do not decode percent escapes.

## Requirements
- Implement `match_route(template, path)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Compare literal segments and capture parameter segments.

## Run tests
`python -m pytest tests -q`
