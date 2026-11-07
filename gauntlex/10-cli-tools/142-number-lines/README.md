# Line Numbers

## Description

Give every input line a sequential label so that a reader can refer to its position. Blank lines count as lines too.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read text lines from standard input.
- Prefix each line with its one-based line number, a colon, and one space.
- Preserve the content of each line, including empty lines.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why does the first line receive label `1` rather than `0`?
- How can a blank line still receive a label?

## Example Input and Output

Input: "a\nb\n"

Expected output: "1: a\n2: b\n"

Input: "\n"

Expected output: "1: \n"
