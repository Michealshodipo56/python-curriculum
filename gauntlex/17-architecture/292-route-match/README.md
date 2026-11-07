# Capture Route Parameters

## Description

HTTP route templates combine fixed path segments with named placeholders. Match a request path and extract the placeholder values.

## Requirements

- Implement `match_route(template, path)` in `starter/solution.py`.
- Accept a route template and request path.
- Require the same number of path segments.
- Match literal segments exactly; capture segments written `{name}` as dictionary entries.
- Return captured values on a match, or `None` on mismatch.
- Do not percent-decode path text.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations

A literal path segment cannot match a different spelling. Capture parameters as raw strings without decoding or numeric conversion.

## Tips

- Why must a literal route segment match exactly?

## Example Behavior

`match_route('/users/{id}', '/users/42')` → `{'id': '42'}`.
