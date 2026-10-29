# circuit_state

## Challenge
Given number of consecutive failures, positive threshold, and bool probe_success, return 'closed' if failures<threshold, 'half-open' if failures>=threshold and probe_success, otherwise 'open'.

## Requirements
- Implement `circuit_state(failures, threshold, probe_success)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Model the three states as explicit cases.

## Run tests
`python -m pytest tests -q`
