# Requests in a Time Window

## Description
A sliding-window rate limit counts recent requests to decide whether another request is permitted. Boundary handling must be exact.

## Requirements
- Implement `rate_limit_allowed(timestamps, now, window, limit)` in `starter/solution.py`.
- Accept sorted integer timestamps, integer `now`, positive `window`, and nonnegative `limit`.
- Count timestamps in the interval `(now - window, now]`.
- Return `True` only when that count is strictly less than `limit`.
- Do not mutate timestamps.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A request exactly at `now - window` is outside the window; a request exactly at `now` is inside. The next request is permitted only below the limit.

## Tips
- Why is the lower boundary excluded but the upper included?

## Example Behavior
`rate_limit_allowed([5, 8, 10], 10, 5, 3)` → `True`, because time 5 is excluded.
