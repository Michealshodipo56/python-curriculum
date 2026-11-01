# Inspect Archive Paths

## Description
Decide whether an archive member name is safe to extract as a relative path.

### Behavior contract
Return True only if a ZIP/TAR member path is a safe nonempty relative POSIX path: no leading slash, backslash, empty segment, dot or dot-dot segment, and no Windows drive prefix such as C:. Do not access the filesystem.

## Requirements
- Implement `archive_member_safe(name)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Check both POSIX traversal and Windows-style absolute prefixes.

The task defines behavior; design the implementation independently.
