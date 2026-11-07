# Keep Valid Records

## Description

Imported records may have missing names or names containing only whitespace. Keep usable records while normalizing their names and preserving other fields.

## Requirements

- Implement `clean_records(records)` in `starter/solution.py`.
- Accept a sequence of record dictionaries.
- Discard records whose `name` is missing, is not a string, or becomes empty after trimming surrounding whitespace.
- Return shallow copies of retained records in their original order, trimming names and preserving other field values.
- Do not modify any original record dictionaries.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips

- How can you check whether a name remains meaningful after trimming?
- Why should output records be distinct from caller-owned dictionaries?

## Example Behavior

`clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}])` → `[{"name": "Ada", "age": 3}]`

`clean_records([])` → `[]`

`clean_records([{"name": None}, {"name": 42}, {"name": " Lin "}])` → `[{"name": "Lin"}]`
