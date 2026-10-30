# file_checksum

## Challenge
Return lowercase SHA-256 hex digest of the raw bytes in a file at the supplied path. Stream the file in chunks instead of reading it all at once.

## Requirements
- Implement `file_checksum(path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Hash bytes in fixed-size chunks.

## Run tests
`python -m pytest tests -q`
