# Load Structured Data

## Description
Read JSON from a UTF-8 file and return its parsed data instead of the original text.

## Requirements
- Implement `read_json_file(path)` in `starter/solution.py`.
- Return the result to the caller; do not print it or request interactive input.
- Use Python's standard library and UTF-8 encoding.
- File paths are provided by the caller; do not hardcode locations.

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
A JSON file can contain an array, object, or scalar. The returned type depends on its contents.
