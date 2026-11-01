# Build a JSON Response

## Description
Wrap serialized JSON data in a small, consistent HTTP-style response object.

### Behavior contract
Return a dictionary with keys `status`, `headers`, and `body`, where status is 200, headers contains `content-type: application/json`, and body is a compact sorted-key JSON string of the supplied value.

## Requirements
- Implement `json_response(value)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`json_response({"b": 2, "a": 1})` → `{"status": 200, "headers": {"content-type": "application/json"}, "body": "{\"a\":1,\"b\":2}"}`

## Tips
The body is a JSON string, not the original Python value.

Examples describe the contract, not a solution.
