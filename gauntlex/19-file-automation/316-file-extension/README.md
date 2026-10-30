# file_extension

## Challenge
Return the lowercase final extension including its dot from a filename. A leading dot on a dotfile does not count as an extension. Return empty string if none.

## Requirements
- Implement `file_extension(filename)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Path suffix handling has special cases for hidden files.

## Run tests
`python -m pytest tests -q`
