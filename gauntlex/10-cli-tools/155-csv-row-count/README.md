# Count CSV Records

## Description

Count data records in a CSV stream while excluding the header row. The result should reflect CSV records, not merely arbitrary text lines.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read CSV input with a header and zero or more data records.
- Do not include the header in the count.
- Print the number of data records followed by a newline.
- Print `0` for empty input or a header-only file.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why does a header not count as a data record?
- What happens when no data rows follow the header?

## Example Input and Output

Input: "name,age\nAda,20\nBob,30\n"

Expected output: "2\n"

Input: "name\n"

Expected output: "0\n"
