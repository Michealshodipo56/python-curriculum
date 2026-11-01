# Count Matching Lines

## Description
Count how many lines contain a supplied literal search string.

### Behavior contract
The first input line is the search string. Count how many subsequent lines contain it as a case-sensitive substring. Print the integer count.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "cat\ncat\ndog\nbobcat\n"

Expected output: "2\n"

Input: "x\na\nb\n"

Expected output: "0\n"

## Tips
A line with several matches still counts only once.

Examples illustrate the output contract, not a solution.
