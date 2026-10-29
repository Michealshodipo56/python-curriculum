# pagination_offset

## Challenge
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
Validate page numbering before calculating the offset.
