# Ensure an Index

## Description
An index can speed up lookups by a frequently searched column. Create a named email index without failing when setup is repeated.

## Requirements
- Implement `ensure_email_index(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `users(email)` exists.
- Ensure an index named `idx_users_email` exists on the `email` column.
- Make repeated calls safe and preserve existing data.
- Do not recreate the table.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why should database setup be idempotent?
- How does an index differ from a table?

## Example Behavior
Calling `ensure_email_index(conn)` twice leaves the named index available without an error.
