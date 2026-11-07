# Find a JSON Field

## Description
Applications frequently receive structured JSON text but need only one field. Parse the document and retrieve the requested object key while handling absent keys.

## Requirements
- Implement `json_value(text, key)` in `starter/solution.py`.
- Decode the supplied JSON text using standard JSON rules.
- Return the value associated with the requested key in the decoded object.
- Return `None` when the requested key is missing; JSON `null` also maps to Python `None`.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Why can missing keys and explicit JSON `null` produce the same result?
- Why is manual string searching unreliable for JSON values?

## Example Behavior
`json_value("{\"a\":1,\"b\":2}", "a")` → `1`

`json_value("{\"x\":null}", "x")` → `None`
