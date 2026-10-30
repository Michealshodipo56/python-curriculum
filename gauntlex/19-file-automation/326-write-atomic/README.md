# write_text_atomic

## Challenge
Write a UTF-8 string to an existing parent directory at the supplied path using a temporary file in the same directory and atomic replacement. Return None. Do not leave temporary files on success.

## Requirements
- Implement `write_text_atomic(path, text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
A temporary file in the destination directory supports atomic replace.

## Run tests
`python -m pytest tests -q`
