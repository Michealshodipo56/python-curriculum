# Count Active Records

## Description
Count JSON records that explicitly declare themselves active. Numeric values that resemble Boolean values must not be mistaken for true.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read valid JSON objects, one per nonempty line.
- Count only objects whose `active` key has the Boolean value `true`.
- Do not count numeric `1`, strings, missing keys, or Boolean `false`.
- Print the count as an integer followed by a newline.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is equality alone potentially misleading when comparing Booleans and integers in Python?
- What happens when a record lacks the key?

## Example Input and Output
Input: "{\"active\":true}\n{\"active\":1}\n{\"active\":false}\n"

Expected output: "1\n"

Input: ""

Expected output: "0\n"
