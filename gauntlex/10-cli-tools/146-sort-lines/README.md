# Order the Lines

## Description

Rearrange complete text lines using case-sensitive lexical order while preserving repeated entries.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read all lines from standard input.
- Sort lines lexicographically by Unicode code point.
- Print each sorted line on its own line, preserving duplicates.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why can uppercase and lowercase letters sort differently?
- Why should duplicate lines remain in the output?

## Example Input and Output

Input: "pear\napple\npear\n"

Expected output: "apple\npear\npear\n"

Input: ""

Expected output: ""
