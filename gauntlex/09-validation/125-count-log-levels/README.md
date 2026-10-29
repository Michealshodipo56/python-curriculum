# count_log_levels

## Description
Given a list of log lines in `LEVEL|YYYY-MM-DD|MESSAGE` format, return counts of valid INFO, WARN and ERROR records, ignoring malformed lines. Include zero counts.

## Requirements
- Implement `count_log_levels(lines)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`count_log_levels(["INFO|2024-01-01|ok", "WARN|2024-01-02|slow", "INFO|2024-01-03|ok", "bad"])` → `{"INFO": 2, "WARN": 1, "ERROR": 0}`

`count_log_levels([])` → `{"INFO": 0, "WARN": 0, "ERROR": 0}`

## Tips
Reuse validation logic rather than assuming every line is well formed.
