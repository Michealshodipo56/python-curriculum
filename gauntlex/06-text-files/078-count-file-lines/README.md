# Read the Line Count

## Description
A file can contain empty lines, a trailing newline, or a final line with no terminator. Read the caller's UTF-8 text file and count its logical lines.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Accept a file path supplied by the caller and open that file using UTF-8.
- Return the number of logical text lines as an integer.
- An empty file has zero lines; a final nonempty line without a newline still counts.
- Do not hardcode a filename or print the count.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why does counting newline characters alone miss a final unterminated line?
- How do you distinguish an empty file from a file containing one blank line?
