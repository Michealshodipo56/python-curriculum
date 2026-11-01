# Safe Relative Paths

## Description
Normalize a relative path without allowing absolute locations or parent traversal.

### Behavior contract
Return a normalized POSIX relative path from text. Reject absolute paths, empty paths, parent (`..`) components, and backslashes with ValueError. Ignore `.` and repeated slashes.

## Requirements
- Implement `safe_relative_path(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Inspect individual path components before normalizing away suspicious segments.

The task defines behavior; design the implementation independently.
