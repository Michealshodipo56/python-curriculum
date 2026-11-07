# First Lines Only

## Description

Build a tool that selects the earliest requested lines from a text stream and discards the remainder.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read a nonnegative integer `N` from the first line.
- Print at most the first `N` subsequent lines, preserving their order and content.
- Print nothing when `N` is zero.
- If fewer than `N` lines remain, print all of them.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- How does the first line differ from the lines being selected?
- What happens when the requested limit exceeds available data?

## Example Input and Output

Input: "2\na\nb\nc\n"

Expected output: "a\nb\n"

Input: "0\na\n"

Expected output: ""
