# Replace a File Safely

## Description
Write text through a temporary file and atomically replace the destination.

### Behavior contract
Write a UTF-8 string to an existing parent directory at the supplied path using a temporary file in the same directory and atomic replacement. Return None. Do not leave temporary files on success.

## Requirements
- Implement `write_text_atomic(path, text)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
The temporary file must share the destination directory to support an atomic replacement.

The task defines behavior; design the implementation independently.
