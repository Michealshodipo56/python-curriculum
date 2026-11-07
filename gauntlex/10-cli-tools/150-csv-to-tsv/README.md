# CSV to Tabs

## Description
Convert comma-separated records into tab-separated records without mistaking commas inside quoted fields for separators.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read CSV records from standard input.
- Interpret quoted commas and escaped double quotation marks using CSV rules.
- Output the same fields separated by tabs, one record per line.
- Assume fields contain no tabs or embedded newlines.
- Produce no extra messages or headers.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is replacing every comma directly unsafe?
- How are quotation marks inside quoted CSV fields represented?

## Example Input and Output
Input: "name,age\nAda,20\n"

Expected output: "name\tage\nAda\t20\n"

Input: "\"a,b\",c\n"

Expected output: "a,b\tc\n"
