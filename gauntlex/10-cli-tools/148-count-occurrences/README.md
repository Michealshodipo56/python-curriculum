# Count Matching Lines

## Description
Count the number of input lines containing a literal search string, rather than the total number of occurrences.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Treat the first input line as the case-sensitive search string.
- Count each subsequent line once if it contains the search string as a substring.
- Print the integer count followed by a newline, including `0` when no lines match.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why must a line with several matches count only once?
- How does literal matching differ from regular-expression matching?

## Example Input and Output
Input: "cat\ncat\ndog\nbobcat\n"

Expected output: "2\n"

Input: "x\na\nb\n"

Expected output: "0\n"
