# Seconds to Clock Text

## Description

Represent a nonnegative number of seconds in a consistent hours-minutes-seconds format.

## Requirements

- Implement `format_duration(seconds)` in `starter/solution.py`.
- Accept a nonnegative integer duration in seconds.
- Return text formatted as `H:MM:SS`.
- Do not pad the hour field; always use exactly two digits for minutes and seconds.
- Raise `ValueError` for a negative duration.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why must minutes and seconds remain below sixty?
- What happens when the hour count has several digits?

## Example Behavior

`format_duration(3723)` → `'1:02:03'`; `format_duration(0)` → `'0:00:00'`.
