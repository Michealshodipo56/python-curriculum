# Extract the Media Type

## Description
A Content-Type header identifies a representation and may also include parameters such as character encoding. Extract only its media type.

## Requirements
- Implement `media_type(header)` in `starter/solution.py`.
- Return the portion of the header before the first semicolon.
- Trim surrounding whitespace and convert the result to lowercase.
- Ignore parameters after the first semicolon.
- Return an empty string for empty input.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why should a charset parameter not be part of the media type?
- What if no semicolon appears?

## Example Behavior
`media_type("Application/JSON; charset=utf-8")` → `"application/json"`

`media_type("text/plain")` → `"text/plain"`
