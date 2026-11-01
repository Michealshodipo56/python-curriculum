# Stay Within Bounds

## Description
Constrain a numeric value to an inclusive interval while detecting invalid interval boundaries.

### Behavior contract
Return value bounded to the inclusive range [low,high]. Raise ValueError when low>high.

## Requirements
- Implement `clamp(value, low, high)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`clamp(12, 0, 10)` → `10`

`clamp(-3, 0, 10)` → `0`

## Tips
Consider values below, within, and above the range. What if the interval itself is impossible?

The examples show required behavior, not an implementation.
