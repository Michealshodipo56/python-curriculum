# parse_boolean

## Description
Return True for 'true','yes','1', False for 'false','no','0', ignoring surrounding whitespace and case. Raise ValueError for other strings.

## Requirements
- Implement `parse_boolean(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_boolean(" YES ")` → `True`

`parse_boolean("No")` → `False`

## Tips
Map accepted tokens to Boolean values; reject ambiguous inputs.
