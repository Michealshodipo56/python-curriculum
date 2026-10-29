# filter_records

## Challenge
Given a list of dictionaries and a mapping of expected key/value pairs, return records matching every pair, preserving order. Empty filters match all records. Return shallow copies.

## Requirements
- Implement `filter_records(records, filters)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`filter_records([{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 2}], {"x": 1})` → `[{"x": 1, "y": 2}, {"x": 1, "y": 3}]`

`filter_records([{"a": 1}], {})` → `[{"a": 1}]`

## Tips
Check all requested fields for each record.
