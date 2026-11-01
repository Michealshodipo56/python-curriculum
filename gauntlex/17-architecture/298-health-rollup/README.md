# Worst Service Health

## Description
Combine individual service health reports into one overall status.

### Behavior contract
Given a list of service status strings 'ok','degraded','down', return 'down' if any is down, else 'degraded' if any is degraded, otherwise 'ok'. Empty list is ok.

## Requirements
- Implement `health_rollup(statuses)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
A single down service dominates degraded and healthy services.

Design your own implementation from the specified behavior.
