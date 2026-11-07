# Safe Relative Paths

## Description

Paths supplied by users must not escape an intended working directory. Normalize harmless separators while rejecting traversal and absolute locations.

## Requirements

- Implement `safe_relative_path(text)` in `starter/solution.py`.
- Reject empty paths, absolute paths, any `..` component, and any backslash with `ValueError`.
- Ignore `.` components and repeated forward slashes.
- Return the remaining components joined as a POSIX relative path.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations

Validate path components before simplifying them: normalizing away `..` first would hide an explicitly forbidden traversal attempt. Treat the output as a relative POSIX path, not a filesystem existence check.

## Tips

- Why must traversal be checked before normalization?

## Example Behavior

`safe_relative_path('a//./b.txt')` → `'a/b.txt'`; `safe_relative_path('../secret')` raises `ValueError`.
