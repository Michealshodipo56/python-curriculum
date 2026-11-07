# Calendar Distance

## Description
Calendar arithmetic must account for varying month lengths and leap years. Determine the absolute number of days separating two supplied dates.

## Requirements
- Implement `days_between(a, b)` in `starter/solution.py`.
- Accept two valid date strings in `YYYY-MM-DD` format.
- Return the nonnegative count of whole calendar days between them.
- Return `0` for the same date, and produce the same distance when arguments are reversed.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why is subtracting day-of-month numbers insufficient?
- What changes when the interval crosses February in a leap year?

## Example Behavior
`days_between("2024-01-01", "2024-01-03")` → `2`

`days_between("2024-03-01", "2024-02-28")` → `2`
