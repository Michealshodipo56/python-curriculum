# Find the Last Header

## Description

HTTP headers may repeat, and header names are case-insensitive. Retrieve the last matching value without changing the original list.

## Requirements

- Implement `header_get(headers, name)` in `starter/solution.py`.
- Accept a list of `[name, value]` pairs and a target header name.
- Compare names without regard to letter case.
- Return the value from the last matching pair, unchanged.
- Return `None` when no header matches.
- Do not modify the input.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips

- Why must the last matching value win?
- How does case-insensitive comparison affect repeated names?

## Example Behavior

`header_get([["X-ID", "1"], ["x-id", "2"]], "X-Id")` → `"2"`

`header_get([["A", "b"]], "X")` → `None`
