# Interpret a Boolean

## Description
Convert common textual representations of yes and no into Boolean values, rejecting unsupported words.

### Behavior contract
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
An invalid token must not silently become false. Distinguish rejection from a legitimate negative response.

The examples show required behavior, not an implementation.
