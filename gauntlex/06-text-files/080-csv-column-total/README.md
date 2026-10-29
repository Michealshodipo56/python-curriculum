# csv_column_total

## Description
Read a UTF-8 CSV file with a header. Return the sum of valid integer cells in a named column.

## Requirements
- Implement `csv_column_total(path, column)` in `starter/solution.py`.
- Return the required value; do not print.
- Use Python's standard library and UTF-8 encoding.
- File paths are provided by the caller; do not hardcode locations.

## Tips
Use a context manager or the pathlib API. Tests create temporary input files.
