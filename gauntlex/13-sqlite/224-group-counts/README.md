# Count Event Categories

## Description
Summarize event frequencies by category and produce a deterministic ranking even when multiple categories have equal counts.

## Requirements
- Implement `group_counts(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read from `events(id,category)`.
- Return `[category, count]` for every distinct category.
- Sort by count descending, then category ascending.
- Return `[]` for an empty table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why should a frequency report specify tie-breaking?
- How does grouping combine multiple rows into one result?

## Example Behavior
If two categories have equal counts, their names determine their order.
