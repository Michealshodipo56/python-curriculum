# Compact JSON Stream

## Description
Process a stream of independent JSON values and output one canonical compact representation for each nonblank record.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read one valid JSON value per nonempty input line.
- Ignore blank input lines.
- Print one compact JSON value per record with object keys sorted alphabetically.
- Do not add unnecessary spaces between JSON separators.
- Preserve the order of records.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why must each line be parsed independently?
- What distinguishes an empty line from a JSON string containing empty text?

## Example Input and Output
Input: "{\"b\":2,\"a\":1}\n\n[1, 2]\n"

Expected output: "{\"a\":1,\"b\":2}\n[1,2]\n"

Input: ""

Expected output: ""
