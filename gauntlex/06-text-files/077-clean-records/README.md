# clean_records

## Description
Return copies of dictionaries whose name field is a nonempty string after trimming, with each retained name trimmed.

## Requirements
- Implement `clean_records(records)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}])` → `[{"name": "Ada", "age": 3}]`

`clean_records([])` → `[]`

## Tips
Create new dictionaries to avoid mutating caller-owned records.
