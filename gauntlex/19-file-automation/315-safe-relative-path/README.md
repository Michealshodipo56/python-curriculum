# safe_relative_path

## Challenge
Return a normalized POSIX relative path from text. Reject absolute paths, empty paths, parent (`..`) components, and backslashes with ValueError. Ignore `.` and repeated slashes.

## Requirements
- Implement `safe_relative_path(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Validate each component, not just the final normalized string.

## Run tests
`python -m pytest tests -q`
