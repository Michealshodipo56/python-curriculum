# Keep Valid Records

## Description
Clean a collection of record dictionaries by retaining only entries with meaningful names.

## Requirements
- Implement `clean_records(records)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}])` → `[{"name": "Ada", "age": 3}]`

`clean_records([])` → `[]`

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
Preserve other fields and avoid changing the caller's original dictionaries.
