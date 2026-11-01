# Describe Build Files

## Description
Produce a sorted manifest of relative file paths and sizes while rejecting unsafe paths.

### Behavior contract
Given a list of [relative_path,bytes_count] pairs, return sorted entries as `path<TAB>bytes` strings. Reject absolute paths and paths containing `..` segments with ValueError.

## Requirements
- Implement `file_manifest(entries)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Path traversal is about complete `..` components, not every occurrence of two dots.

The learner must develop the implementation from the stated contract.
