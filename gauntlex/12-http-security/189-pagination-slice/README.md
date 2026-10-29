# paginate

## Challenge
Return the items belonging to 1-based page of size page_size. Raise ValueError for invalid page or size. Do not mutate items.

## Requirements
- Implement `paginate(items, page, page_size)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`paginate([1, 2, 3, 4, 5], 2, 2)` → `[3, 4]`

`paginate([1, 2], 3, 2)` → `[]`

## Tips
Use the calculated offset as a slice start.
