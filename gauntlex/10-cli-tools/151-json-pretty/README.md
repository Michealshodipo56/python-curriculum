# Readable JSON

## Description

Turn compact JSON into a human-readable representation while preserving its data. The output must use predictable indentation and key ordering.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read one valid JSON value from standard input.
- Print valid JSON with object keys sorted alphabetically and indentation of two spaces.
- End the output with exactly one newline.
- Support JSON arrays, objects, and scalar values.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why can two differently formatted JSON strings represent the same value?
- What makes output formatting predictable?

## Example Input and Output

Input: "{\"b\":2,\"a\":1}\n"

Expected output: "{\n  \"a\": 1,\n  \"b\": 2\n}\n"

Input: "[1,2]\n"

Expected output: "[\n  1,\n  2\n]\n"
