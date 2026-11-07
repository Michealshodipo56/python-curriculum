# Structured Log Entry

## Description

A log entry combines a severity, a date, and a message. Parse these fields without losing separators that belong to the message itself.

## Requirements

- Implement `parse_log_line(line)` in `starter/solution.py`.
- Accept records formatted `LEVEL|YYYY-MM-DD|MESSAGE`.
- Require `LEVEL` to be exactly `INFO`, `WARN`, or `ERROR`.
- Require a real calendar date in the specified format.
- Allow the message to contain additional `|` characters; only the first two pipes separate fields.
- Return a dictionary with `level`, `date`, and `message`, or `None` for invalid input.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why is splitting at every delimiter unsafe for the message?
- Why must a date be checked beyond its visual pattern?

## Example Behavior

`parse_log_line('INFO|2024-02-29|Started|ok')` → `{'level': 'INFO', 'date': '2024-02-29', 'message': 'Started|ok'}`; `parse_log_line('DEBUG|2024-01-01|x')` → `None`.
