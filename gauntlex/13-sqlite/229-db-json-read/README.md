# Load a JSON Document

## Description
Retrieve a stored JSON document and restore its structured Python representation rather than returning raw serialized text.

## Requirements
- Implement `load_json(conn, doc_id)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read the `body` field from `documents(id,body TEXT)` for the requested ID.
- Decode the stored JSON text to a Python value.
- Return `None` if the row does not exist.
- Do not modify the database.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why is a stored JSON string different from its decoded Python value?
- What does a missing record mean?

## Example Behavior
A missing document ID returns `None`; a stored JSON object is returned as a Python dictionary.
