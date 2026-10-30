# count_file_lines

## Challenge
Return the number of logical text lines in a UTF-8 file. A nonempty final line without a newline counts as one; empty file has zero lines. Universal newline handling is allowed.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Iterating over an opened text file yields logical lines.

## Run tests
`python -m pytest tests -q`
