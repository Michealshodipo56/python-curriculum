# Three Text Measures

## Description

Report three different measurements of an input stream: logical lines, whitespace-separated words, and Unicode characters.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read all text from standard input.
- Print the number of lines as determined by Python's `splitlines()` behavior.
- Print the number of whitespace-separated words.
- Print the total number of Unicode characters, including spaces and newline characters.
- Output the three integers on separate lines, each ending with a newline.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why do spaces and line breaks contribute to the character count?
- How does the number of words differ from the number of lines?

## Example Input and Output

Input: "a b\nc\n"

Expected output: "2\n3\n6\n"

Input: ""

Expected output: "0\n0\n0\n"
