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

## Tips
- Why is a relative POSIX path more portable than an absolute local path?

## Example Behavior
A root containing `a.txt` and `docs/b.txt` produces `['a.txt', 'docs/b.txt']`.
