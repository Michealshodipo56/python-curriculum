# Map a Directory

## Description
A directory manifest describes all regular files below a root using portable relative paths. Traverse subdirectories without following directory symlinks.

## Requirements
- Implement `directory_manifest(root)` in `starter/solution.py`.
- Recursively find regular files beneath the supplied root directory.
- Return their paths relative to the root using POSIX forward slashes.
- Sort the resulting path strings alphabetically.
- Exclude directories and do not follow directory symlinks.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Traverse directories recursively but do not descend into symlinked directories. Express every discovered regular file as a POSIX path relative to the supplied root and sort the completed list.

## Tips
- Why is a relative POSIX path more portable than an absolute local path?

## Example Behavior
A root containing `a.txt` and `docs/b.txt` produces `['a.txt', 'docs/b.txt']`.
