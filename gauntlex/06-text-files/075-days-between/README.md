# Calendar Distance

## Description
Measure the number of whole days separating two valid dates, regardless of which comes first.

## Requirements
- Implement `days_between(a, b)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`days_between("2024-01-01", "2024-01-03")` → `2`

`days_between("2024-03-01", "2024-02-28")` → `2`

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
Dates have calendar rules that ordinary numeric subtraction does not capture.
