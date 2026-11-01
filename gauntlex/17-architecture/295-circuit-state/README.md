# Circuit Breaker States

## Description
Classify a service circuit as closed, open, or half-open using failures and a probe outcome.

### Behavior contract
Given number of consecutive failures, positive threshold, and bool probe_success, return 'closed' if failures<threshold, 'half-open' if failures>=threshold and probe_success, otherwise 'open'.

## Requirements
- Implement `circuit_state(failures, threshold, probe_success)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Model the threshold and probe as separate decisions.

Design your own implementation from the specified behavior.
