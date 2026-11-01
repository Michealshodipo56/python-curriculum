# Requests in a Time Window

## Description
Determine whether another request is allowed under a sliding-window rate limit.

### Behavior contract
Given sorted integer request timestamps, current integer time, positive window, and nonnegative limit, return True if fewer than limit requests occurred in the half-open interval (now-window,now].

## Requirements
- Implement `rate_limit_allowed(timestamps, now, window, limit)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
The lower time boundary is exclusive while the upper boundary is inclusive.

Design your own implementation from the specified behavior.
