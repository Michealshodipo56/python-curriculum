# flatten_json

## Challenge
Flatten nested dictionaries into a mapping of dot-separated keys to leaf values. Lists count as leaves. Empty dictionaries count as leaves. Assume input keys are nonempty strings without dots.

## Requirements
- Implement `flatten_json(data)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Recursively visit dictionaries and keep the current key prefix.

## Run tests
`python -m pytest tests -q`
