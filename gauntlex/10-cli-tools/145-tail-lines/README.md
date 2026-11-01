# Last Lines Only

## Description
Select the final requested lines of a stream while preserving their order.

### Behavior contract
Read a nonnegative integer N from the first line, then print at most the last N remaining input lines in their original order.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "2\na\nb\nc\n"

Expected output: "b\nc\n"

Input: "0\na\n"

Expected output: ""

## Tips
The final two lines should remain in their original order, not be reversed.

Examples illustrate the output contract, not a solution.
