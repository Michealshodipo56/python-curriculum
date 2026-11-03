# Stay Within Bounds

## Description
Constrain a number to a specified inclusive interval. Values outside the interval should be brought to the nearest boundary, while invalid bounds must be rejected.

## Requirements
- Implement `clamp(value, low, high)` in `starter/solution.py`.
- Accept numeric `value`, `low`, and `high` arguments.
- Return `low` if the value is below it, or `high` if above it.
- Return the original value when it is already within the inclusive interval.
- Raise `ValueError` when `low > high`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- How do the three possible positions relative to an interval differ?
- What happens when the two bounds are equal?

## Example Behavior
`clamp(12, 0, 10)` → `10`; `clamp(-3, 0, 10)` → `0`.
