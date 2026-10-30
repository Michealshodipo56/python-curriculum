# Contact Book

## Project brief and acceptance criteria
Build SQLite contact book. CONTACT_DB specifies path. Commands: add NAME EMAIL, find TERM, delete EMAIL, list. Emails are unique case-insensitively; retain original casing. add prints ok or exists; delete prints ok or not found. list and find print compact sorted-key JSON arrays of {name,email}, sorted by lowercase email; find matches case-insensitive substrings in name or email. Empty names/emails exit 2.

## Deliverables
Implement in starter/main.py, add unit tests and document architecture. Python 3.11+ standard library only. No network services. Do not print debug output to stdout. Use parameterized SQL where applicable.

## Run
python -m pytest tests -q
