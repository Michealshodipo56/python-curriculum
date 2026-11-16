# Describe Build Files

## Description

Implement `file_manifest(entries)` in `starter/solution.py`. Reject absolute paths and paths containing a complete `..` segment with `ValueError`.

## Requirements

- Implement `file_manifest(entries)` in `starter/solution.py`.
- Accept `[relative_path, bytes_count]` pairs.
- Reject absolute paths and paths containing a complete `..` segment with `ValueError`.
- Return sorted strings formatted `path<TAB>bytes`.
- Do not modify the entries.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- **Concept to understand:** A build manifest records the files included in an artifact and their byte counts. Reject paths that could escape the intended relative directory.
- Why is a `..` path component different from two dots inside a filename?

## Example Behavior

`file_manifest([['b.txt', 2], ['a.txt', 5]])` → `['a.txt\t5', 'b.txt\t2']`.
