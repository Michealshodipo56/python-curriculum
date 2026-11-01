# Dependency Order

## Description
Sort exact package requirements by normalized name while preserving each original line.

### Behavior contract
Given valid exact requirements `name==version`, return them sorted by normalized package name, preserving the original requirement text.

## Requirements
- Implement `sort_requirements(lines)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
The sort key and the returned text are intentionally different.

The learner must develop the implementation from the stated contract.
