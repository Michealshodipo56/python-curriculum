# Real Calendar Dates

## Description
Accept a date string only if it describes an actual day on the calendar.

## Requirements
- Implement `parse_date(text)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`parse_date("2024-02-29")` → `"2024-02-29"`

`parse_date("2023-02-29")` → `None`

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
Check leap years and impossible day numbers; matching a date pattern alone is not enough.
