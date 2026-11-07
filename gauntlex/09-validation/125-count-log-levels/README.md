# Log Severity Summary

## Description

Summarize the severity of valid structured log records while ignoring malformed lines. The output must include every supported severity even when its count is zero.

## Requirements

- Implement `count_log_levels(lines)` in `starter/solution.py`.
- Accept a list of log lines formatted `LEVEL|YYYY-MM-DD|MESSAGE`; additional pipes belong to the message.
- Count only valid `INFO`, `WARN`, and `ERROR` records.
- Ignore malformed lines, including invalid calendar dates.
- Return a dictionary containing all three level names with integer counts.
- Do not modify `lines`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why is checking the prefix alone insufficient to validate a record?
- What should the result contain for an empty list?

## Example Behavior

`count_log_levels(['INFO|2024-01-01|ok', 'WARN|2024-01-02|slow', 'INFO|2024-01-03|ok', 'bad'])` → `{'INFO': 2, 'WARN': 1, 'ERROR': 0}`.
