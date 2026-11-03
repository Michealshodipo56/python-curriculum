# Canonical URL Paths

## Description
Normalize a POSIX-style URL path into a stable rooted form. Redundant separators and relative segments should not allow the result to escape above the root.

## Requirements
- Implement `normalize_url_path(path)` in `starter/solution.py`.
- Return a path beginning with `/`.
- Collapse repeated slashes and remove `.` segments.
- Resolve `..` segments by removing a preceding ordinary segment when possible.
- Never navigate above the root.
- Remove a trailing slash unless the result is `/`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- What should happen when a parent segment appears at the root?
- How do `.` and `..` differ?

## Example Behavior
`normalize_url_path('/a//b/./c/../d')` → `'/a/b/d'`; `normalize_url_path('../../x')` → `'/x'`.
