# Match Every Field

## Description
Filter structured records by a set of exact key-value requirements.

### Behavior contract
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
A record matches only when all requested fields agree; empty criteria match everything.

Examples describe the contract, not a solution.
