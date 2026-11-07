# Configuration Assignments

## Description
Read configuration assignments from multiline text. Ignore blank and comment lines, normalize surrounding whitespace, and allow later assignments to replace earlier ones.

## Requirements
- Implement `parse_env(text)` in `starter/solution.py`.
- Interpret noncomment lines as `KEY=VALUE` assignments.
- Ignore blank lines and lines whose first nonspace character is `#`.
- Trim whitespace around keys and values.
- Split each assignment at its first `=` so the value may contain additional equals signs.
- Raise `ValueError` for any noncomment, nonblank line without `=`.
- Keep the last value for repeated keys.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should only the first equals sign separate the key and value?
- What makes a line a comment rather than an assignment?

## Example Behavior
`parse_env('A=1\nB = hello world\n# comment\nA=2')` → `{'A': '2', 'B': 'hello world'}`.
