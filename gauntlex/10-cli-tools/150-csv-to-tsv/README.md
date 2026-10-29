# csvtotsv

## Challenge
Read CSV records from standard input and print equivalent tab-separated records. Assume fields contain no tabs or embedded newlines, but may contain quoted commas and escaped double quotes.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "name,age\nAda,20\n"

Expected output: "name\tage\nAda\t20\n"

Input: "\"a,b\",c\n"

Expected output: "a,b\tc\n"

## Hints
Use the standard library CSV reader for correct quoted-field parsing.
