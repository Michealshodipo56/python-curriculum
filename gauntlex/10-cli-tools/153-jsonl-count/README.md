# Count Active Records

## Description
Read JSON objects and count only those explicitly marked active with a Boolean true value.

### Behavior contract
Read valid JSON objects, one per nonempty line. Print the count of objects containing the key `active` with Boolean value true.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "{\"active\":true}\n{\"active\":1}\n{\"active\":false}\n"

Expected output: "1\n"

Input: ""

Expected output: "0\n"

## Tips
In Python, a numeric one and Boolean true can compare equal; the contract distinguishes their types.

Examples illustrate the output contract, not a solution.
