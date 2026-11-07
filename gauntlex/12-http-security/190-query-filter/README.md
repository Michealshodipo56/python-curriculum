# Match Every Field

## Description

Select dictionary records that match every exact field requirement.

## Requirements

- Implement `filter_records(records, filters)` in `starter/solution.py`.
- Return only records matching all key-value pairs in `filters`.
- Preserve original record order.
- Treat empty filters as matching all records.
- Return shallow copies without mutating inputs.
- Use Python's standard library without printing or making network requests.

## Tips

- Why does a single mismatched field disqualify a record?

## Example Behavior

`filter_records([{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 2}], {"x": 1})` → `[{"x": 1, "y": 2}, {"x": 1, "y": 3}]`

`filter_records([{"a": 1}], {})` → `[{"a": 1}]`
