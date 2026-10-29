# jsonpretty

## Challenge
Read one JSON value from standard input. Print it as JSON with sorted object keys, an indentation width of 2, and a final newline. Input is valid JSON.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "{\"b\":2,\"a\":1}\n"

Expected output: "{\n  \"a\": 1,\n  \"b\": 2\n}\n"

Input: "[1,2]\n"

Expected output: "[\n  1,\n  2\n]\n"

## Hints
The JSON encoder can sort keys and indent output.
