# Day of the Week

## Description
Translate a calendar date into the ISO weekday numbering system.

## Requirements
- Implement `iso_weekday(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`iso_weekday("2024-01-01")` → `1`

`iso_weekday("2024-01-07")` → `7`

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
ISO weeks start on Monday. Check both the beginning and end of a week.
