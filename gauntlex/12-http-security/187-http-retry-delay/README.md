# Backoff with a Ceiling

## Description
When a request fails, successive retries can wait progressively longer. Calculate an exponential delay without exceeding a maximum permitted interval.

## Requirements
- Implement `retry_delay(attempt, base, cap)` in `starter/solution.py`.
- Assume `attempt` is nonnegative and both `base` and `cap` are positive.
- Return the smaller of `cap` and `base * 2**attempt`, measured in seconds.
- Do not sleep, print, or make any network requests.

## Tips
- The first attempt uses the base delay; each successive attempt doubles the uncapped delay.
- Consider when the cap prevents further growth.

## Example Behavior
`retry_delay(0, 0.5, 10)` → `0.5`

`retry_delay(3, 0.5, 10)` → `4`
