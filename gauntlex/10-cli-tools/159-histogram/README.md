# Value Histogram

## Description

Count how often each nonnegative integer occurs in a stream, then display a frequency report sorted by value.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read whitespace-separated nonnegative integers from standard input.
- Count occurrences of each distinct value.
- Print one line per distinct value in ascending numeric order, formatted `VALUE: COUNT`.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why does sorting by value differ from sorting by frequency?
- How should repeated values affect the count?

## Example Input and Output

Input: "3 1 3 2 1 3\n"

Expected output: "1: 2\n2: 1\n3: 3\n"

Input: ""

Expected output: ""
