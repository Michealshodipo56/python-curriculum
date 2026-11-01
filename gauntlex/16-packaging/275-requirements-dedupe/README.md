# One Requirement per Package

## Description
Remove repeated package requirements, keeping the final entry for each normalized name.

### Behavior contract
Given valid exact requirements, return one per normalized package name, keeping the last occurrence and preserving the order of surviving last occurrences.

## Requirements
- Implement `dedupe_requirements(lines)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
The order of surviving last occurrences matters.

The learner must develop the implementation from the stated contract.
