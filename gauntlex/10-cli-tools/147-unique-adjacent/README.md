# uniqadjacent

## Challenge
Read all lines and print only the first line in each run of consecutive identical lines. A repeated line after a different line must be printed again.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "a\na\nb\na\na\n"

Expected output: "a\nb\na\n"

Input: "\n\nx\n"

Expected output: "\nx\n"

## Hints
Compare each line with the immediately previous line, not with all prior lines.
