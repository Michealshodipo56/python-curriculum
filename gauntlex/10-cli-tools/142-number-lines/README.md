# Line Numbers

## Description
Add an ordered label to each line of text without changing the line's content.

### Behavior contract
Read all lines from standard input and prefix each line with its 1-based line number followed by a colon and one space.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "a\nb\n"

Expected output: "1: a\n2: b\n"

Input: "\n"

Expected output: "1: \n"

## Tips
A blank line is still a line. The first label should be one, not zero.

Examples illustrate the output contract, not a solution.
