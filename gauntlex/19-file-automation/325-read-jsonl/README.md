# Load a JSON Lines Stream

## Description
JSON Lines files contain one independent JSON document per nonblank line. Read the stream in order while allowing malformed JSON to surface as an error.

## Requirements
- Implement `read_jsonl(path)` in `starter/solution.py`.
- Read the file as UTF-8 text.
- Skip blank or whitespace-only lines.
- Parse every other line as a JSON value and return the values in original order.
- Propagate JSON decoding errors rather than silently ignoring invalid records.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why must each line be decoded independently?

## Example Behavior
A file with lines `{"a":1}`, blank, and `[2,3]` produces `[{'a': 1}, [2, 3]]`.
