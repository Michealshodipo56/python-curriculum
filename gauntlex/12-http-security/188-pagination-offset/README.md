# Page to Offset

## Description
Translate a one-based page number into a zero-based record offset.

### Behavior contract
Return offset for 1-based page and positive page_size: (page-1)*page_size. Raise ValueError if either is not positive.

## Requirements
- Implement `pagination_offset(page, page_size)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`pagination_offset(1, 20)` → `0`

`pagination_offset(3, 20)` → `40`

## Tips
Page one begins at offset zero. Invalid page sizes must be rejected.

Examples describe the contract, not a solution.
