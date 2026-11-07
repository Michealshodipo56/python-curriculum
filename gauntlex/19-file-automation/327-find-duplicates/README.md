# Find Duplicate Content

## Description

Files with different names can contain identical bytes. Group duplicate content by SHA-256 fingerprints rather than comparing filenames.

## Requirements

- Implement `duplicate_hashes(paths)` in `starter/solution.py`.
- Accept a list of file paths.
- Hash each file's raw bytes with SHA-256.
- Return a dictionary from lowercase digest strings to sorted path strings.
- Include only digests associated with more than one supplied path.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations

Group files by digest of raw bytes, then omit groups containing only one supplied path. Sort path strings within every retained group so the result does not depend on traversal order.

## Tips

- Why is file size or filename alone insufficient to identify duplicates?

## Example Behavior

Two distinct paths containing the same bytes appear together under one digest; a unique file is omitted.
