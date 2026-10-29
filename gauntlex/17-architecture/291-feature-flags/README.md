# enabled_features

## Challenge
Given a mapping of feature names to booleans and a mapping of feature dependencies to lists, return sorted enabled feature names whose own flag and every transitive dependency flag are true. Missing flags count as false. Assume the dependency graph is acyclic.

## Requirements
- Implement `enabled_features(flags, dependencies)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
A feature can be enabled only when its entire prerequisite chain is enabled.

## Run tests
`python -m pytest tests -q`
