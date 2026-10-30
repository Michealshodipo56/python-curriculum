# normalize_line_endings

## Challenge
Convert CRLF and standalone CR line endings to LF. Preserve all other characters, including trailing newlines.

## Requirements
- Implement `normalize_line_endings(text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Replace CRLF first, then remaining CR.

## Run tests
`python -m pytest tests -q`
