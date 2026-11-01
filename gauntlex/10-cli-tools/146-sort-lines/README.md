# Order the Lines

## Description
Rearrange complete input lines using case-sensitive lexical ordering.

### Behavior contract
Read all input lines, sort them lexicographically by Unicode code point, and print each on a separate line. Preserve duplicate lines.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "pear\napple\npear\n"

Expected output: "apple\npear\npear\n"

Input: ""

Expected output: ""

## Tips
Sorting is based on characters rather than numeric meaning; duplicates remain.

Examples illustrate the output contract, not a solution.
