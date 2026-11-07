# Search Names Literally

## Description

A name search should treat the search term as text, even when it contains characters that SQL ordinarily uses as wildcards.

## Requirements

- Implement `search_users(conn, term)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Search names case-insensitively for the supplied substring.
- Treat `%` and `_` as literal characters, not pattern wildcards.
- Return `[id, name]` rows ordered by ascending ID.
- Return `[]` if no names match.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips

- Why does binding a LIKE pattern not automatically make its wildcard characters literal?
- How can a search be case-insensitive without losing the input text?

## Example Behavior

A term containing `%` searches for the percent character itself rather than matching arbitrary text.
