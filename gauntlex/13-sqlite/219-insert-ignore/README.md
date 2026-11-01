# Insert Only Once

## Description
Add a user only when their unique email does not already exist.

### Behavior contract
Insert (name,email) into users(id,name,email UNIQUE). Return True only when a new row was inserted; duplicate emails must not raise and must not overwrite.

## Requirements
- Implement `insert_email_once(conn, name, email)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
A duplicate should neither overwrite existing data nor be reported as a new insert.

Implement the database behavior without using solution code from another task.
