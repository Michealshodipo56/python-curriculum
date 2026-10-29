# format_duration

## Description
Format nonnegative integer seconds as `H:MM:SS`, with unpadded hours and exactly two digits each for minutes and seconds. Raise ValueError for negative seconds.

## Requirements
- Implement `format_duration(seconds)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`format_duration(3723)` → `"1:02:03"`

`format_duration(0)` → `"0:00:00"`

## Tips
Integer division and remainders split a total into hours, minutes and seconds.
