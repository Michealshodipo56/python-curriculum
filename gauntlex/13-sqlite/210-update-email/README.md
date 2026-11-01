# Change a User Email

## Description
Update a stored email address and report whether a user was actually affected.

### Behavior contract
Update the email of a user by integer ID. Return True if a row was updated, otherwise False. Table users(id,name,email) exists.

## Requirements
- Implement `update_email(conn, user_id, email)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
The outcome should distinguish a successful update from an absent user.

Design the database interaction yourself; no SQL solution is provided.
