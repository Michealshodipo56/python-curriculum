# Day of the Week

## Description

Scheduling systems often represent weekdays numerically. Translate a valid calendar date to the ISO convention instead of relying on locale-specific weekday names.

## Requirements

- Implement `iso_weekday(text)` in `starter/solution.py`.
- Accept a valid date string in `YYYY-MM-DD` format.
- Return the ISO weekday as an integer from `1` (Monday) through `7` (Sunday).
- Use the actual calendar date rather than inferring weekdays from the day-of-month number.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips

- How does ISO numbering differ from systems that start weeks on Sunday?
- What weekday value should consecutive dates produce?

## Example Behavior

`iso_weekday("2024-01-01")` → `1`

`iso_weekday("2024-01-07")` → `7`
