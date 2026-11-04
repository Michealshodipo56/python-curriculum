# Last Lines Only

## Description
Build a tool that selects the final requested lines of a stream without reversing their order.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read a nonnegative integer `N` from the first line.
- Print at most the last `N` subsequent lines in their original order.
- Print nothing when `N` is zero.
- If fewer than `N` lines remain, print all of them.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is choosing the last lines different from reversing the stream?
- What happens when the requested limit is larger than the input?

## Example Input and Output
Input: "2\na\nb\nc\n"

Expected output: "b\nc\n"

Input: "0\na\n"

Expected output: ""
