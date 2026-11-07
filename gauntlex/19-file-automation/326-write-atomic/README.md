# Replace a File Safely

## Description
Writing directly to a destination risks leaving partial content if a write is interrupted. Prepare replacement content in the same directory before switching files.

## Requirements
- Implement `write_text_atomic(path, text)` in `starter/solution.py`.
- Write the supplied string as UTF-8.
- Use a temporary file in the destination's existing parent directory.
- Atomically replace the destination with the completed temporary file.
- Return `None`; leave no temporary file after a successful replacement.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why should the temporary file be created on the same filesystem as the destination?

## Example Behavior
Writing `'ready\n'` to an existing destination replaces its previous contents with exactly `ready` followed by a newline.
