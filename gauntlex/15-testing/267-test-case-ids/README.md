# Unique Case Labels

## Description

Repeated test names need distinct identifiers so reports can refer to each occurrence without ambiguity.

## Requirements

- Implement `case_ids(cases)` in `starter/solution.py`.
- Accept test case dictionaries containing a string `name`.
- Assign each name its own one-based occurrence counter.
- Return IDs in original case order, formatted as `name#N`.
- Do not mutate case dictionaries.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why must different names have independent counters?

## Example Behavior

`case_ids([{'name': 'a'}, {'name': 'b'}, {'name': 'a'}])` → `['a#1', 'b#1', 'a#2']`.
