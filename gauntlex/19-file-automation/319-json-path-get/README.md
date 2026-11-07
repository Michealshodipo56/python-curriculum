# Follow Nested Keys

## Description

Structured data often contains nested mappings. Navigate a dot-separated key path without assuming list indices are supported.

## Requirements

- Implement `json_path_get(data, path)` in `starter/solution.py`.
- An empty path returns the original object.
- For a nonempty path, interpret each dot-separated component as a dictionary key.
- Return `None` when a required key is missing or traversal cannot continue through a dictionary.
- Do not interpret numeric components as list indices.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations

At each path component, verify that the current value is a dictionary before attempting key lookup. A dictionary key containing digits is still a key, never a list position.

## Tips

- Why should a missing intermediate key stop traversal?

## Example Behavior

`json_path_get({'user': {'name': 'Ada'}}, 'user.name')` → `'Ada'`; missing path → `None`.
