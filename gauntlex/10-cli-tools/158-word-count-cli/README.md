# wordcountcli

## Challenge
Read arbitrary text from standard input. Print three integers on separate lines: line count using splitlines(), whitespace-separated word count, and total Unicode character count.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "a b\nc\n"

Expected output: "2\n3\n6\n"

Input: ""

Expected output: "0\n0\n0\n"

## Hints
Read the complete input text once, then calculate each metric.
