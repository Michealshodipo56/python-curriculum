# Final File Suffix

## Description
Extract the final extension of a POSIX filename, ignoring the case of its letters.

## Requirements
- Implement `path_extension(path)` in `starter/solution.py`.
- Return the result to the caller without printing or requesting interactive input.
- Handle the boundary cases implied by the examples and description.
- Use Python's standard library only.
- Preserve caller-owned input values and collections.

## Example Behavior
`path_extension("notes.TXT")` → `"txt"`

`path_extension("archive.tar.gz")` → `"gz"`

## Tips
- Identify the input type, output type, and exact format before implementing the function.
- Consider empty or minimal input alongside the supplied examples.
Consider filenames with multiple dots and filenames without an extension.
