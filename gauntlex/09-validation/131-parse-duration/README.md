# Clock Text to Seconds

## Description
Interpret a duration expressed in hours, minutes, and seconds, rejecting malformed notation.

### Behavior contract
Parse a duration formatted as `H:MM:SS`, where H is a nonnegative integer and MM and SS are exactly two digits from 00 to 59. Return total seconds. Raise ValueError on invalid input.

## Requirements
- Implement `parse_duration(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_duration("1:02:03")` → `3723`

`parse_duration("0:00:05")` → `5`

## Tips
Validate minute and second bounds before combining the three units.

The examples specify results without giving an implementation.
