# Events After a Date

## Description
Canonical ISO dates can be compared lexically when their format is consistent. Select events from a cutoff date onward.

## Requirements
- Implement `events_on_or_after(conn, cutoff)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume valid `YYYY-MM-DD` strings in `events(id,event_date TEXT)` and in the cutoff.
- Include events on or after the cutoff date.
- Return `[id, event_date]` rows ordered by event date, then ID.
- Do not modify the table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why do zero-padded ISO dates have useful lexical ordering?
- Why is the cutoff inclusive?

## Example Behavior
An event dated exactly on the cutoff is included; an earlier event is excluded.
