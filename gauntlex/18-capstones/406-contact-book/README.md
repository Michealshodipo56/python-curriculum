# Contact Directory

## Description

Build a persistent contact book with case-insensitive email uniqueness and searchable names and addresses.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run commands from `starter/` as `python main.py add NAME EMAIL`, `python main.py find TERM`, `python main.py delete EMAIL`, or `python main.py list`.
- Persist contacts in SQLite at the path supplied by `CONTACT_DB` across separate process runs.
- Enforce case-insensitive email uniqueness while retaining each stored email's original spelling.
- `add` prints `ok` for a new contact or `exists` for a duplicate email without replacing the original contact.
- `delete` matches email case-insensitively and prints `ok` or `not found`.
- `list` and `find` print compact JSON arrays of objects with `name` and `email`, with sorted object keys and records sorted by lowercase email.
- `find` matches a case-insensitive substring in either the name or email. A search with no matches and an empty directory produce `[]`.
- Empty names or emails exit with status `2` without inserting. End each printed result with a newline.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain case-insensitive uniqueness, searches, and display ordering.

## Design Considerations

Store original email spelling while enforcing uniqueness and lookups case-insensitively. Sort records by normalized email, not by display name.

## Example Behavior

After adding `Ada@Example.com`, adding `ada@example.com` returns `exists` without creating a second contact.

## Tips

Preserve original email spelling while comparing addresses case-insensitively.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
