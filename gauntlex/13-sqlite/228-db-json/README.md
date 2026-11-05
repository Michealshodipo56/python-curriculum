# Store a JSON Document

## Description
Structured Python data can be persisted as JSON text. Use a stable representation so equivalent dictionaries serialize consistently.

## Requirements
- Implement `store_json(conn, value)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `documents(id INTEGER PRIMARY KEY,body TEXT)` exists.
- Serialize the supplied JSON-compatible value with sorted object keys and compact separators.
- Store the resulting JSON string in the `body` column.
- Return the new document's integer row ID.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why is Python's display representation not a substitute for JSON?
- How does stable key ordering help reproducibility?

## Example Behavior
Storing `{'b': 2, 'a': 1}` saves the compact JSON body `{"a":1,"b":2}`.
