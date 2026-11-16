# Pinned Dependency

## Description

Implement `parse_requirement(text)` in `starter/solution.py`. Allow ASCII letters, digits, underscores, and hyphens in the name.

## Requirements

- Implement `parse_requirement(text)` in `starter/solution.py`.
- Accept exactly `name==version`.
- Allow ASCII letters, digits, underscores, and hyphens in the name.
- Require three dot-separated nonnegative integer components in the version.
- Return `[normalized_name, version]` where the name is lowercase and underscores become hyphens.
- Raise `ValueError` for invalid input.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- **Concept to understand:** A pinned dependency specifies one package and one exact version. Normalize the package name while retaining the version text.
- Why should package-name normalization be distinct from version validation?

## Example Behavior

`parse_requirement('My_Pkg==1.2.3')` → `['my-pkg', '1.2.3']`.
