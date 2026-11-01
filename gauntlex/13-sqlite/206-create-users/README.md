# Define the Users Table

## Description
Establish a database table that can safely store users and enforce uniqueness of their email addresses.

### Behavior contract
Create a users table if absent, with id INTEGER PRIMARY KEY, name TEXT NOT NULL, and email TEXT NOT NULL UNIQUE.

## Requirements
- Implement `create_users(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
Which rules belong in the schema so every future insert must respect them?

Design the database interaction yourself; no SQL solution is provided.
