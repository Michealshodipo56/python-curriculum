# read_jsonl

## Challenge
Read a UTF-8 JSON Lines file and return parsed values in order, skipping blank or whitespace-only lines. Propagate JSON decoding errors.

## Requirements
- Implement `read_jsonl(path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Parse one nonblank line at a time.

## Run tests
`python -m pytest tests -q`
