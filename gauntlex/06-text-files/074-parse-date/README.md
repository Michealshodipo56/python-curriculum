# Real Calendar Dates

## Description
A date-like string is not necessarily a real date. Validate calendar rules, including month lengths and leap years, before accepting it.

## Requirements
- Implement `parse_date(text)` in `starter/solution.py`.
- Interpret date text in the `YYYY-MM-DD` calendar format.
- Return the validated date string for a real date.
- Return `None` when the date is invalid, including impossible days such as February 29 in a nonleap year.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why does a matching pattern not prove that a date exists?
- Which years permit February 29?

## Example Behavior
`parse_date("2024-02-29")` → `"2024-02-29"`

`parse_date("2023-02-29")` → `None`
