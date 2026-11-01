# Find Matching Lines

## Description
Build a literal text search that returns matching lines in their original order.

### Behavior contract
The first input line is a case-sensitive search string. Print every subsequent input line containing that string, in original order.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "cat\ncatapult\ndog\nbobcat\n"

Expected output: "catapult\nbobcat\n"

Input: "z\nabc\n"

Expected output: ""

## Tips
Search for a substring, not a whole word or a regular expression.

Examples illustrate the output contract, not a solution.
