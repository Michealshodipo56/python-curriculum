# Recognize HTTP Methods

## Description
Normalize a request method to a standard uppercase spelling, then reject names outside a fixed set of supported HTTP methods.

## Requirements
- Implement `normalize_method(text)` in `starter/solution.py`.
- Trim surrounding whitespace and ignore the input's letter case.
- Return the uppercase method if it is GET, POST, PUT, PATCH, DELETE, HEAD, or OPTIONS.
- Raise `ValueError` for all other values, including an empty string.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why is normalization useful before checking allowed methods?
- Why should an unsupported method be rejected explicitly?

## Example Behavior
`normalize_method(" get ")` → `"GET"`

`normalize_method("PaTcH")` → `"PATCH"`
