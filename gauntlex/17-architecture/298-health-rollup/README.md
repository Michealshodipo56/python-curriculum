# health_rollup

## Challenge
Given a list of service status strings 'ok','degraded','down', return 'down' if any is down, else 'degraded' if any is degraded, otherwise 'ok'. Empty list is ok.

## Requirements
- Implement `health_rollup(statuses)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Choose the worst observed status.

## Run tests
`python -m pytest tests -q`
