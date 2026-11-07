# Measure the Failure Rate

## Description

Repeated test runs can reveal instability. Summarize the proportion of unsuccessful runs rather than the count alone.

## Requirements

- Implement `failure_rate(results)` in `starter/solution.py`.
- Accept a sequence of booleans where `True` means success and `False` means failure.
- Return the number of failures divided by the number of runs.
- Return `0.0` when there are no runs.
- Do not change the results.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why does a fraction make results comparable across different run counts?

## Example Behavior

`failure_rate([True, False, False, True])` → `0.5`; `failure_rate([])` → `0.0`.
