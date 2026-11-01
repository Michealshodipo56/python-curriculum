# First Lines Only

## Description
Limit a stream to its earliest requested lines, leaving the rest out.

### Behavior contract
Read a nonnegative integer N from the first line, then print at most the first N remaining input lines.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "2\na\nb\nc\n"

Expected output: "a\nb\n"

Input: "0\na\n"

Expected output: ""

## Tips
Zero is a valid limit and should produce no output.

Examples illustrate the output contract, not a solution.
