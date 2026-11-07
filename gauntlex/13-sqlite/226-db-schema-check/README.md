# Inspect the Schema

## Description
A database can contain tables, views, and indexes. Determine whether a named object is specifically a table, not merely any schema entry.

## Requirements
- Implement `table_exists(conn, table_name)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Check the SQLite schema for the supplied table name.
- Return `True` only if an actual table with that name exists.
- Return `False` for missing names, views, and indexes.
- Treat the name as data rather than interpolating it into arbitrary SQL.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why does the presence of a schema name not guarantee a table exists?
- Which object type must be checked?

## Example Behavior
A named view must produce `False`, even if its name exists in the SQLite schema.
