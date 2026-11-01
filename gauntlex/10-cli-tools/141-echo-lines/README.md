# Reverse the Stream

## Description
Read an entire stream of lines and replay them in the opposite order.

### Behavior contract
Read all lines from standard input and print them in reverse order, preserving the content of each line but using a single newline per output line.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "red\nblue\ngreen\n"

Expected output: "green\nblue\nred\n"

Input: ""

Expected output: ""

## Tips
Think about why reversing lines requires remembering input before producing output.

Examples illustrate the output contract, not a solution.
