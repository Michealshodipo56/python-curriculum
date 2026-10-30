# directory_manifest

## Challenge
Given a directory path, recursively return sorted relative POSIX paths of all regular files beneath it. Exclude directories and do not follow directory symlinks.

## Requirements
- Implement `directory_manifest(root)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Use pathlib recursion and convert relative paths to POSIX separators.

## Run tests
`python -m pytest tests -q`
