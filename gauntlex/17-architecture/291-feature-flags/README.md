# Transitive Feature Gates

## Description
Determine which features can actually be enabled when their own flags and dependencies must all be active.

### Behavior contract
Given a mapping of feature names to booleans and a mapping of feature dependencies to lists, return sorted enabled feature names whose own flag and every transitive dependency flag are true. Missing flags count as false. Assume the dependency graph is acyclic.

## Requirements
- Implement `enabled_features(flags, dependencies)` in `starter/solution.py`.
- Return the specified result without printing.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
A feature may be switched on yet unavailable because one prerequisite is off.

Design your own implementation from the specified behavior.
