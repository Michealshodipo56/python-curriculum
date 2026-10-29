# jsonlines

## Challenge
Read one valid JSON value per nonempty input line. Print one compact sorted-key JSON value per nonempty line; skip blank lines.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "{\"b\":2,\"a\":1}\n\n[1, 2]\n"

Expected output: "{\"a\":1,\"b\":2}\n[1,2]\n"

Input: ""

Expected output: ""

## Hints
Process each record independently rather than parsing the whole stream as one JSON value.
