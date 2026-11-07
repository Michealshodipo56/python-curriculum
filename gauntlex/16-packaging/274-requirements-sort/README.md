# Dependency Order

## Description

A dependency file can be made easier to review by sorting package entries consistently, while preserving their original spelling and version text.

## Requirements

- Implement `sort_requirements(lines)` in `starter/solution.py`.
- Accept valid exact requirement strings `name==version`.
- Sort requirements by their normalized package names.
- Return the original requirement strings, not rewritten versions.
- Do not mutate the original sequence.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why should the comparison key differ from the text returned to the caller?

## Example Behavior

`sort_requirements(['Zed==1.0.0', 'alpha==2.0.0'])` → `['alpha==2.0.0', 'Zed==1.0.0']`.
