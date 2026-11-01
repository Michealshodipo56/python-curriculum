# Find the Last Header

## Description
Retrieve the final value of a named HTTP header, matching its name without regard to case.

### Behavior contract
Given a list of [name,value] HTTP header pairs and a name, return the last matching header value ignoring name case, or None when absent.

## Requirements
- Implement `header_get(headers, name)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`header_get([["X-ID", "1"], ["x-id", "2"]], "X-Id")` → `"2"`

`header_get([["A", "b"]], "X")` → `None`

## Tips
Duplicate header names are possible; the last matching value takes precedence.

Examples describe the contract, not a solution.
