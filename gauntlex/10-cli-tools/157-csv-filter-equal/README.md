# Filter CSV Records

## Description
Filter CSV data records using an exact field comparison and emit each match as a compact JSON object.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read the column name and exact target value from the first two input lines.
- Treat the remaining input as CSV with a header row.
- Select only records whose named field exactly equals the target.
- Print matching records as compact JSON objects with alphabetically sorted keys, one per line.
- Preserve input record order and print nothing when there are no matches.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why should capitalization and whitespace matter for an exact match?
- How can the header provide JSON field names?

## Example Input and Output
Input: "city\nLagos\nname,city\nAda,Lagos\nBob,Abuja\n"

Expected output: "{\"city\":\"Lagos\",\"name\":\"Ada\"}\n"

Input: "status\nok\nname,status\nx,no\n"

Expected output: ""
