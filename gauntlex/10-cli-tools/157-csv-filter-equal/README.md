# Filter CSV Records

## Description
Select records whose named field matches a target value and encode each match as JSON.

### Behavior contract
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

## Tips
Exact matching should not confuse values with similar spelling or capitalization.

Examples illustrate the output contract, not a solution.
