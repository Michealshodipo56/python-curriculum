# Flatten a JSON Tree

## Description
Turn nested dictionaries into dot-separated key paths while retaining their leaf values.

### Behavior contract
Flatten nested dictionaries into a mapping of dot-separated keys to leaf values. Lists count as leaves. Empty dictionaries count as leaves. Assume input keys are nonempty strings without dots.

## Requirements
- Implement `flatten_json(data)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
Empty dictionaries and lists have special treatment as leaves.

The task defines behavior; design the implementation independently.
