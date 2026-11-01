# Rebuild Nested JSON

## Description
Reconstruct nested dictionaries from a mapping of dot-separated key paths.

### Behavior contract
Given a flat mapping of dot-separated paths to leaf values, construct nested dictionaries. Assume no paths conflict (e.g. a and a.b), and keys are nonempty.

## Requirements
- Implement `unflatten_json(data)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Create intermediate mappings only when needed.

The task defines behavior; design the implementation independently.
