# One Page of Results

## Description

Select a page of records from a collection without changing the original.

## Requirements

- Implement `paginate(items, page, page_size)` in `starter/solution.py`.
- Accept a one-based page and positive page size.
- Raise `ValueError` for invalid page or size.
- Return the selected items in their original order.
- Return `[]` for a page beyond the available records.
- Do not mutate the collection.
- Use Python's standard library without printing or making network requests.

## Tips

- How should a partially filled final page behave?

## Example Behavior

`paginate([1, 2, 3, 4, 5], 2, 2)` → `[3, 4]`

`paginate([1, 2], 3, 2)` → `[]`
