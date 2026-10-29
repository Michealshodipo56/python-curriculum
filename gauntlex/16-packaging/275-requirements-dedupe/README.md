# dedupe_requirements

## Challenge
Given valid exact requirements, return one per normalized package name, keeping the last occurrence and preserving the order of surviving last occurrences.

## Requirements
- Implement `dedupe_requirements(lines)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Record each package's last index before filtering.

## Run tests
`python -m pytest tests -q`
