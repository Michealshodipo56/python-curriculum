# Numeric Stream Summary

## Description
Summarize an integer stream using its count, total, minimum, and maximum. Empty input has a deliberately shorter report.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read whitespace-separated integers from standard input.
- For nonempty input, print four lines in this exact order: `count=N`, `sum=S`, `min=M`, `max=X`.
- For empty input, print only `count=0` and `sum=0`.
- End every printed line with a newline and do not print additional text.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why are minimum and maximum undefined for an empty stream?
- How should negative and repeated values affect each statistic?

## Example Input and Output
Input: "3 1 2\n"

Expected output: "count=3\nsum=6\nmin=1\nmax=3\n"

Input: ""

Expected output: "count=0\nsum=0\n"
