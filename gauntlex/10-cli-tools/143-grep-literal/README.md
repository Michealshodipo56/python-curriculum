# Find Matching Lines

## Description

Create a simple literal search tool that filters a stream of text lines by a case-sensitive substring.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Treat the first input line as the literal search string.
- Inspect every remaining input line for that exact substring.
- Print matching lines in their original order, once per matching line.
- Do not print the search string itself or lines without a match.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why is a substring match different from a whole-word match?
- What does case-sensitive matching imply?

## Example Input and Output

Input: "cat\ncatapult\ndog\nbobcat\n"

Expected output: "catapult\nbobcat\n"

Input: "z\nabc\n"

Expected output: ""
