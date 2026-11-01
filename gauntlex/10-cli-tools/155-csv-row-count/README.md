# Count CSV Records

## Description
Count data records in a CSV stream without counting its header.

### Behavior contract
Read CSV with a header row and zero or more data records. Print the number of data records. Empty input produces 0.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "name,age\nAda,20\nBob,30\n"

Expected output: "2\n"

Input: "name\n"

Expected output: "0\n"

## Tips
An empty stream and a header-only stream both have zero data records.

Examples illustrate the output contract, not a solution.
