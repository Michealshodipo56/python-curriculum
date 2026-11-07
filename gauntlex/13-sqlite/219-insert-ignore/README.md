# Insert Only Once

## Description
Add a user only when the email is not already registered. A duplicate must leave the existing record intact.

## Requirements
- Implement `insert_email_once(conn, name, email)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `users(id,name,email UNIQUE)` exists.
- Return `True` only if a new row is inserted.
- For an existing email, return `False` without raising or overwriting the record.
- Bind name and email as data parameters.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- How can uniqueness be enforced by the database?
- Why is ignoring a duplicate different from replacing a record?

## Example Behavior
Registering the same email twice returns `True` and then `False`, without changing the first record.
