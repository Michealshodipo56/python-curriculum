# Final File Suffix

## Description
A filename can contain several dots or none at all. Identify its final suffix without confusing earlier filename segments with the extension.

## Requirements
- Implement `path_extension(path)` in `starter/solution.py`.
- Inspect the final filename component of the supplied POSIX path.
- Return the final extension in lowercase without the leading dot.
- Return an empty string when there is no extension; do not treat a lone leading dot as an ordinary extension.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why is the final dot more relevant than the first dot?
- How should a hidden file without a second dot be treated?

## Example Behavior
`path_extension("notes.TXT")` → `"txt"`

`path_extension("archive.tar.gz")` → `"gz"`
