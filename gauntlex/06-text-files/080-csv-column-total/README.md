# Sum a CSV Column

## Description
Process a CSV table with a header and add the valid integer values in a chosen column.

## Requirements
- Implement `csv_column_total(path, column)` in `starter/solution.py`.
- Return the result to the caller; do not print it or request interactive input.
- Use Python's standard library and UTF-8 encoding.
- File paths are provided by the caller; do not hardcode locations.

## Tips
- Identify the expected input, output, and failure or empty-data behavior before implementing the function.
- Check the exact behavior at boundaries, not only typical inputs.
Identify the requested column by its header rather than relying on a fixed position.
