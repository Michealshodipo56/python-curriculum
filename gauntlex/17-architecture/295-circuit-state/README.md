# Circuit Breaker States

## Description
A circuit breaker tracks consecutive failures and may allow a recovery probe. Classify the state from the failure threshold and probe result.

## Requirements
- Implement `circuit_state(failures, threshold, probe_success)` in `starter/solution.py`.
- Accept a failure count, positive threshold, and boolean `probe_success`.
- Return `'closed'` when failures are below the threshold.
- At or above the threshold, return `'half-open'` for a successful probe, otherwise `'open'`.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
When failures are below threshold, the state remains closed regardless of probe outcome; the probe matters only at or above threshold.

## Tips
- Why must the failure threshold be checked before the probe outcome?

## Example Behavior
`circuit_state(3, 3, False)` → `'open'`; `circuit_state(3, 3, True)` → `'half-open'`.
