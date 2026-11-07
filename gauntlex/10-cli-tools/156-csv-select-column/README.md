# Extract a CSV Column

## Description

Select a CSV column by its header name rather than by a fixed numeric position. Preserve the order of data rows.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read the target column name from the first input line.
- Treat the remaining input as CSV with a header row.
- Assume the named column exists and fields contain no embedded newlines.
- Print that column's value for each data row on its own line, in original row order.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why should the header determine which field is selected?
- How does an empty field affect the output?

## Example Input and Output

Input: "name\nname,age\nAda,20\nBob,30\n"

Expected output: "Ada\nBob\n"

Input: "age\nname,age\nAda,20\n"

Expected output: "20\n"
