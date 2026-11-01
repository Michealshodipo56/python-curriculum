# Follow Nested Keys

## Description
Navigate a structured JSON-compatible object using a dot-separated path of dictionary keys.

### Behavior contract
Given a JSON-compatible object and a dot-separated path of dictionary keys, return the nested value or None if any key is absent. An empty path returns the original object. Do not interpret list indices.

## Requirements
- Implement `json_path_get(data, path)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
A missing key stops traversal; an empty path refers to the original value.

The task defines behavior; design the implementation independently.
