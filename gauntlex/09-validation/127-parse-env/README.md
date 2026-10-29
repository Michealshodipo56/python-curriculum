# parse_env

## Description
Parse lines of KEY=VALUE assignments into a dictionary. Ignore blank lines and lines whose first non-space character is #. Trim whitespace around keys and values. Reject noncomment lines without = using ValueError. Later keys overwrite earlier ones.

## Requirements
- Implement `parse_env(text)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`parse_env("A=1\nB = hello world\n# comment\nA=2")` → `{"A": "2", "B": "hello world"}`

`parse_env("  \n#x")` → `{}`

## Tips
Split each assignment only at the first equals sign.
