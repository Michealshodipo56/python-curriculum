# Inspect Archive Paths

## Description
Archive member names can contain traversal or platform-specific absolute paths. Validate the name before it could be used for extraction.

## Requirements
- Implement `archive_member_safe(name)` in `starter/solution.py`.
- Return `True` only for nonempty relative POSIX member names.
- Reject leading slashes, backslashes, empty segments, `.` segments, and `..` segments.
- Reject Windows drive prefixes such as `C:`.
- Do not read or write any files.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why must Windows-style paths be rejected even on a POSIX system?

## Example Behavior
`archive_member_safe('docs/readme.md')` → `True`; `archive_member_safe('../secret')` → `False`.
