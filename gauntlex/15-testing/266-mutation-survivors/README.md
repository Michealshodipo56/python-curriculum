# Undetected Mutations

## Description

Mutation testing changes a program deliberately to see whether tests detect the change. A mutant survives when every supplied test still passes.

## Requirements

- Implement `surviving_mutants(results)` in `starter/solution.py`.
- Accept a mapping from mutant IDs to lists of boolean test outcomes.
- Return sorted mutant IDs whose entire outcome list contains only `True`.
- Treat an empty outcome list as surviving, because no test detected the mutant.
- Return `[]` when no mutants survive.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why does a mutant with no test outcomes count as undetected?

## Example Behavior

`surviving_mutants({'m1': [True, True], 'm2': [True, False], 'm3': []})` → `['m1', 'm3']`.
