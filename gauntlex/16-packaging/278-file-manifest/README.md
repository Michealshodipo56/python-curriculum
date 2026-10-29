# file_manifest

## Challenge
Given a list of [relative_path,bytes_count] pairs, return sorted entries as `path<TAB>bytes` strings. Reject absolute paths and paths containing `..` segments with ValueError.

## Requirements
- Implement `file_manifest(entries)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Validate each path component rather than searching for a substring.

## Run tests
`python -m pytest tests -q`
