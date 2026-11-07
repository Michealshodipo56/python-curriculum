# Page to Offset

## Description

Convert a one-based page number into the zero-based position of its first record.

## Requirements

- Implement `pagination_offset(page, page_size)` in `starter/solution.py`.
- Return the offset for positive `page` and `page_size`.
- Raise `ValueError` if either is nonpositive.
- Page one begins at offset zero.
- Use Python's standard library without printing or making network requests.

## Tips

- Why do two pages precede page three?

## Example Behavior

`pagination_offset(1, 20)` → `0`

`pagination_offset(3, 20)` → `40`
