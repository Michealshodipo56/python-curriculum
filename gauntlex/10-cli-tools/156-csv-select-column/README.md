# csvselect

## Challenge
The first input line contains the target column name. Remaining input is CSV with a header. Print values from that column, one per data row. Assume the column exists and fields contain no newlines.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "name\nname,age\nAda,20\nBob,30\n"

Expected output: "Ada\nBob\n"

Input: "age\nname,age\nAda,20\n"

Expected output: "20\n"

## Hints
A DictReader maps header names to field values.
