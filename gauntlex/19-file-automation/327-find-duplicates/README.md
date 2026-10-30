# duplicate_hashes

## Challenge
Given a list of file paths, return a dictionary mapping SHA-256 hex digests to sorted path strings, but only for digests occurring more than once. Read file bytes; do not rely on filenames.

## Requirements
- Implement `duplicate_hashes(paths)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Group paths by content digest, then keep only groups of size at least two.

## Run tests
`python -m pytest tests -q`
