# Read the Response Status

## Description
Interpret a status line into its numeric status and human-readable reason.

### Behavior contract
Parse an HTTP/1.1 status line like `HTTP/1.1 200 OK` into a dictionary with integer status and string reason. Return None for malformed input.

## Requirements
- Implement `parse_status_line(line)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`parse_status_line("HTTP/1.1 200 OK")` → `{"status": 200, "reason": "OK"}`

`parse_status_line("HTTP/1.1 404 Not Found")` → `{"status": 404, "reason": "Not Found"}`

## Tips
The reason phrase can contain spaces, so a simple split into every word is insufficient.

Examples describe the contract, not a solution.
