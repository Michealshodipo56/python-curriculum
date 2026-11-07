# Contact Directory

## Description
Build a persistent contact book with case-insensitive email uniqueness and searchable names and addresses.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Build SQLite contact book. CONTACT_DB specifies path. Commands: add NAME EMAIL, find TERM, delete EMAIL, list. Emails are unique case-insensitively; retain original casing. add prints ok or exists; delete prints ok or not found. list and find print compact sorted-key JSON arrays of {name,email}, sorted by lowercase email; find matches case-insensitive substrings in name or email. Empty names/emails exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Store original email spelling while enforcing uniqueness and lookups case-insensitively. Sort records by normalized email, not by display name.

## Example Behavior
After adding `Ada@Example.com`, adding `ada@example.com` returns `exists` without creating a second contact.

## Tips
Preserve original email spelling while comparing addresses case-insensitively.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
