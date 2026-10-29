# clamp

## Description
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
Check the range invariant before applying lower and upper bounds.
