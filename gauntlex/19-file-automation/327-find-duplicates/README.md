# Find Duplicate Content

## Description
Group files with identical byte content by their cryptographic digest.

### Behavior contract
Given a list of file paths, return a dictionary mapping SHA-256 hex digests to sorted path strings, but only for digests occurring more than once. Read file bytes; do not rely on filenames.

## Requirements
- Implement `duplicate_hashes(paths)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Different filenames can contain the same bytes, and equal names can contain different bytes.

The task defines behavior; design the implementation independently.
