# Structured Log Entry

## Description
Interpret a line containing a severity, calendar date, and free-form message, rejecting malformed records.

### Behavior contract
Parse a log line formatted `LEVEL|YYYY-MM-DD|MESSAGE`. Return a dict with keys level, date, message, or None if invalid. LEVEL must be INFO, WARN or ERROR; date must be a real calendar date. MESSAGE may contain |.

## Requirements
- Implement `parse_log_line(line)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_log_line("INFO|2024-02-29|Started|ok")` → `{"level": "INFO", "date": "2024-02-29", "message": "Started|ok"}`

`parse_log_line("DEBUG|2024-01-01|x")` → `None`

## Tips
The message may contain delimiters, so dividing at every delimiter loses information.

The examples show required behavior, not an implementation.
