# Protect the Retry Budget

## Description
Calculate how many retries remain under a policy based on request volume.

### Behavior contract
Given a nonnegative request count, nonnegative ratio, and nonnegative retries already used, return the maximum of zero and floor(requests*ratio)-retries_used.

## Requirements
- Implement `retry_budget(requests, ratio, retries_used)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
A budget cannot become negative after retries have been spent.

Design your own implementation from the specified behavior.
