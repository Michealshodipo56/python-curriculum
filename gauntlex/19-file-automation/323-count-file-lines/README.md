# Count File Records

## Description
A logical line may end with a newline or at end-of-file. Count both forms correctly when reading UTF-8 text.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Read a UTF-8 text file.
- Return the number of logical lines, including a final nonempty line without a newline.
- Return zero for an empty file.
- Universal newline handling is permitted.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why does counting newline characters alone miss some final lines?

## Example Behavior
A file containing `alpha\nbeta` has two logical lines; an empty file has zero.
