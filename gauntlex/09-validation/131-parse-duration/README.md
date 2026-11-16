# Clock Text to Seconds

## Description

Implement `parse_duration(text)` in `starter/solution.py`. Require exactly two digits each for minutes and seconds.

## Requirements

- Implement `parse_duration(text)` in `starter/solution.py`.
- Accept `H:MM:SS` with a nonnegative integer hour field.
- Require exactly two digits each for minutes and seconds.
- Require minutes and seconds to be between `00` and `59` inclusive.
- Return the total duration in seconds.
- Raise `ValueError` for invalid notation or out-of-range components.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- **Concept to understand:** Interpret a duration in hours, minutes, and seconds. Reject malformed text and impossible minute or second values.
- Why must minutes and seconds be bounded independently of hours?
- What is the difference between an invalid format and a valid zero duration?

## Example Behavior

`parse_duration('1:02:03')` → `3723`; `parse_duration('0:00:05')` → `5`.
