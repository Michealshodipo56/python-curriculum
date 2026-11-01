# Map a Directory

## Description
Create a sorted inventory of regular files beneath a directory.

### Behavior contract
Given a directory path, recursively return sorted relative POSIX paths of all regular files beneath it. Exclude directories and do not follow directory symlinks.

## Requirements
- Implement `directory_manifest(root)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Directory symlinks should not lead the traversal outside the intended tree.

The task defines behavior; design the implementation independently.
