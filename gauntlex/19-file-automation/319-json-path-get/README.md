# json_path_get

## Challenge
Given a JSON-compatible object and a dot-separated path of dictionary keys, return the nested value or None if any key is absent. An empty path returns the original object. Do not interpret list indices.

## Requirements
- Implement `json_path_get(data, path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Descend one dictionary key at a time.

## Run tests
`python -m pytest tests -q`
