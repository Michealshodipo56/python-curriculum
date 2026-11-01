# Sum the Stream

## Description
Accumulate all integers from a multi-line text stream into one total.

### Behavior contract
Read zero or more nonempty lines, each containing whitespace-separated integers. Print the sum of every integer across all lines.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "1 2\n3 4\n"

Expected output: "10\n"

Input: ""

Expected output: "0\n"

## Tips
A line can contain several values; an empty stream still has a well-defined sum.

Examples illustrate the output contract, not a solution.
