# jsonlselect

## Challenge
The first input line contains a key name. Each subsequent nonempty line is a valid JSON object. Print the value for that key as compact JSON, one per matching record; skip objects without the key.

## Requirements
- Implement in `starter/main.py` using standard input and standard output.
- Print no prompts, debug messages, or explanatory text.
- Use the Python standard library only.
- Match the required output exactly, including line endings.

## Examples
Input: "name\n{\"name\":\"Ada\",\"age\":3}\n{\"age\":4}\n{\"name\":null}\n"

Expected output: "\"Ada\"\nnull\n"

Input: "x\n{}\n"

Expected output: ""

## Hints
Distinguish an absent key from a present key with null value.
