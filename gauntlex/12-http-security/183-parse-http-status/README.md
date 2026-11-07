# Read the Response Status

## Description
Interpret an HTTP/1.1 response status line as a numeric status and a potentially multiword reason.

## Requirements
- Implement `parse_status_line(line)` in `starter/solution.py`.
- Return a dictionary with integer `status` and string `reason` for valid HTTP/1.1 status lines.
- Return `None` for malformed input.
- Preserve the full reason phrase, including internal spaces.
- Use the Python standard library, without printing or making network requests.

## Tips
- Why is splitting every word insufficient for a reason such as `Not Found`?

## Example Behavior
`parse_status_line("HTTP/1.1 200 OK")` → `{"status": 200, "reason": "OK"}`

`parse_status_line("HTTP/1.1 404 Not Found")` → `{"status": 404, "reason": "Not Found"}`
