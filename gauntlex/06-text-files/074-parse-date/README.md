# Real Calendar Dates

## Description
Accept a date string only if it describes an actual day on the calendar.

## Requirements
- Implement `parse_date(text)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`parse_date("2024-02-29")` → `"2024-02-29"`

`parse_date("2023-02-29")` → `None`

## Tips
Check leap years and impossible day numbers; matching a date pattern alone is not enough.

Examples describe expected behavior without providing the implementation.
