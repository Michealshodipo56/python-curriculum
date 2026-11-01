# Keep Valid Records

## Description
Clean a collection of record dictionaries by retaining only entries with meaningful names.

## Requirements
- Implement `clean_records(records)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}])` → `[{"name": "Ada", "age": 3}]`

`clean_records([])` → `[]`

## Tips
Preserve other fields and avoid changing the caller's original dictionaries.

Examples describe expected behavior without providing the implementation.
