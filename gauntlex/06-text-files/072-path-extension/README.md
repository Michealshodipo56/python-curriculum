# path_extension

## Description
Return the lowercase final filename extension without the dot, or empty string if absent. POSIX paths.

## Requirements
- Implement `path_extension(path)` in `starter/solution.py`.
- Return the required value without printing or prompting.
- Use the standard library only and do not mutate input collections.

## Examples
`path_extension("notes.TXT")` → `"txt"`

`path_extension("archive.tar.gz")` → `"gz"`

## Tips
Path suffixes differ from the text after the first dot.
