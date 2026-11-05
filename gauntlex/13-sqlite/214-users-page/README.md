# Paginate User Records

## Description
A large directory is easier to consume in pages. Select a consistent slice of users by their IDs.

## Requirements
- Implement `users_page(conn, page, page_size)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Accept a one-based page and a positive page size.
- Raise `ValueError` for nonpositive page or page size.
- Return `[id, name]` rows ordered by ascending ID.
- Return `[]` for a page beyond available records.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- Why is an explicit ordering necessary for stable pagination?|What is the offset of the first page?

## Example Behavior
For users with IDs 1–5, page 2 of size 2 returns the records with IDs 3 and 4.
