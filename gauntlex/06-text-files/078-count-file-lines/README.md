# Read the Line Count

## Description
Open a text file supplied by the caller and report how many logical lines it contains.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Return the result to the caller; do not print it or request interactive input.
- Use Python's standard library and UTF-8 encoding.
- File paths are provided by the caller; do not hardcode locations.

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
File content and file paths are different inputs. Consider empty files and trailing newlines.
