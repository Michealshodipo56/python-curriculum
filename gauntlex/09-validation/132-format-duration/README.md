# Seconds to Clock Text

## Description
Convert a nonnegative duration into a consistent hours-minutes-seconds representation.

### Behavior contract
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
Hours may exceed two digits; minutes and seconds must always occupy two digits.

The examples specify results without giving an implementation.
