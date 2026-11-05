# Build a JSON Response

## Description
Wrap an arbitrary JSON-serializable value in a predictable HTTP-style response object.

## Requirements
- Implement `json_response(value)` in `starter/solution.py`.
- Return a dictionary with `status`, `headers`, and `body`.
- Set status to `200` and `headers` to `{'content-type': 'application/json'}`.
- Encode the body as compact JSON text with sorted object keys.
- Do not return the original value as the body.
- Use Python's standard library without printing or making network requests.

## Tips
- Why is a serialized JSON body different from a Python dictionary?

## Example Behavior
`json_response({"b": 2, "a": 1})` → `{"status": 200, "headers": {"content-type": "application/json"}, "body": "{\"a\":1,\"b\":2}"}`
