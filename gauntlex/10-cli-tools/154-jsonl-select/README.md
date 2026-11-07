# Extract JSON Fields

## Description

Extract one named field from a stream of JSON objects. Missing fields are skipped, but explicitly null fields must remain in the output.

## Requirements

- Implement the program in `starter/main.py` using standard input and standard output.
- Read the desired key name from the first input line.
- Treat subsequent nonempty lines as valid JSON objects.
- Print the value for the named key as compact JSON, one line per matching object.
- Skip objects without the key, but print `null` when the key is present with a null value.
- Preserve record order.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips

- Why is a missing key different from a key containing null?
- Why should strings be printed as JSON strings rather than raw text?

## Example Input and Output

Input: "name\n{\"name\":\"Ada\",\"age\":3}\n{\"age\":4}\n{\"name\":null}\n"

Expected output: "\"Ada\"\nnull\n"

Input: "x\n{}\n"

Expected output: ""
