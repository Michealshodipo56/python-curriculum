# csvfilter

## Challenge
The first two input lines are column name and exact target value. Remaining input is CSV with a header. Print matching data records as compact JSON objects with sorted keys, one per line.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "city\nLagos\nname,city\nAda,Lagos\nBob,Abuja\n"

Expected output: "{\"city\":\"Lagos\",\"name\":\"Ada\"}\n"

Input: "status\nok\nname,status\nx,no\n"

Expected output: ""

## Hints
A DictReader and a JSON encoder make output independent of CSV column order.
