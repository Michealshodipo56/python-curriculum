# Load Structured Data

## Description

Structured configuration and data files may contain objects, arrays, or scalar JSON values. Load the actual Python value rather than returning unparsed text.

## Requirements

- Implement `read_json_file(path)` in `starter/solution.py`.
- Accept a caller-supplied file path and read it as UTF-8 text.
- Parse the file as JSON and return the decoded Python value.
- Support any valid JSON root type, including objects, arrays, strings, numbers, booleans, and null.
- Do not hardcode paths or print the parsed result.
- Use Python's standard library only. Do not mutate caller-owned inputs.
- Assume an existing readable file containing valid JSON; custom file-error recovery is outside this challenge.

## Tips

- Why should the function not assume that every JSON document starts with `{`?
- What Python values correspond to JSON booleans and null?

## Example Behavior

For a UTF-8 file containing `{"ok": true, "count": 3}`, `read_json_file(path)` returns `{'ok': True, 'count': 3}`.
