# Protect the Retry Budget

## Description

Retries consume resources and should remain proportional to normal request traffic. Calculate how many attempts are still permitted.

## Requirements

- Implement `retry_budget(requests, ratio, retries_used)` in `starter/solution.py`.
- Accept nonnegative request count, retry ratio, and retries already used.
- Compute the allowed retry count as the floor of `requests * ratio`.
- Subtract used retries and never return a negative number.
- Return the remaining retry count as an integer.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

The retry allowance is rounded down before subtracting used attempts; exhausted budgets return zero rather than a negative count.

## Tips

- Why should a retry budget never become negative?

## Example Behavior

`retry_budget(10, 0.3, 1)` → `2`.
