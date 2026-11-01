# CSV to Tabs

## Description
Convert structured comma-separated records into tab-separated output without corrupting quoted fields.

### Behavior contract
Read CSV records from standard input and print equivalent tab-separated records. Assume fields contain no tabs or embedded newlines, but may contain quoted commas and escaped double quotes.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "name,age\nAda,20\n"

Expected output: "name\tage\nAda\t20\n"

Input: "\"a,b\",c\n"

Expected output: "a,b\tc\n"

## Tips
Quoted commas belong to a field, not to the separators between fields.

Examples illustrate the output contract, not a solution.
