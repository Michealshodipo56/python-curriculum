# Register a User

## Description
Register one new person in the existing users table and return the database-generated identity of that record.

## Requirements
- Implement `insert_user(conn, name, email)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Assume the `users(id,name,email)` table already exists.
- Insert the supplied name and email without constructing SQL from string concatenation.
- Return the inserted row's integer ID.
- Let database constraints reject invalid or duplicate records.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- Why should user-supplied text be bound as a parameter?
- How can you identify the row that was just created?

## Example Behavior
After `insert_user(conn, 'Ada', 'ada@example.com')`, the returned integer identifies the new row.
