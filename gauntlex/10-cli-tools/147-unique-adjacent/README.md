# Collapse Repeated Lines

## Description
Remove duplicates only when they appear consecutively. A value that returns after a different line must appear again.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read all lines from standard input.
- Keep only the first line in each consecutive run of identical lines.
- Preserve the original order of retained lines.
- Treat blank lines as ordinary lines for comparison.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is this different from removing every duplicate globally?
- What happens when an earlier line reappears after another line?

## Example Input and Output
Input: "a\na\nb\na\na\n"

Expected output: "a\nb\na\n"

Input: "\n\nx\n"

Expected output: "\nx\n"
