# Extract the Media Type

## Description
Separate a Content-Type header's media type from optional parameters.

### Behavior contract
Return the lowercase media type before the first semicolon in a Content-Type header, trimming surrounding whitespace. Return empty string for empty input.

## Requirements
- Implement `media_type(header)` in `starter/solution.py`.
- Return the required value; do not print or prompt.
- Use Python's standard library only; do not make real network requests.
- Preserve inputs without mutation.

## Examples
`media_type("Application/JSON; charset=utf-8")` → `"application/json"`

`media_type("text/plain")` → `"text/plain"`

## Tips
The part before the first semicolon identifies the media type.

Examples describe the contract, not a solution.
