# Recognize HTTP Methods

## Description
Normalize supported HTTP method names and reject unknown methods.

### Behavior contract
Return the uppercase method if it is one of GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, ignoring surrounding whitespace and case. Otherwise raise ValueError.

## Requirements
- Implement `normalize_method(text)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`normalize_method(" get ")` → `"GET"`

`normalize_method("PaTcH")` → `"PATCH"`

## Tips
Normalize spelling before checking membership in the allowed set.

Examples describe the contract, not a solution.
