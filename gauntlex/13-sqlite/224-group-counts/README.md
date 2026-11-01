# Count Event Categories

## Description
Aggregate event records by category and return a stable frequency ranking.

### Behavior contract
Return [category,count] for rows in events(id,category), ordered by count descending then category ascending.

## Requirements
- Implement `group_counts(conn)` in `starter/solution.py`.
- The `conn` argument is a live `sqlite3.Connection` supplied by the caller.
- Do not open a new database connection or print output.
- Use parameterized SQL for untrusted values and standard-library modules only.
- Preserve the caller's existing data and transaction state except for the documented changes.

## Tips
Two categories with equal counts still need a predictable ordering.

Implement the database behavior without using solution code from another task.
