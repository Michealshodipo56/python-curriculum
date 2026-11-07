# One Requirement per Package

## Description

A dependency list may mention the same normalized package multiple times. Keep the final declaration for each package while preserving surviving declaration order.

## Requirements

- Implement `dedupe_requirements(lines)` in `starter/solution.py`.
- Accept valid exact requirement strings.
- Treat names as equivalent after lowercase conversion and replacing underscores with hyphens.
- Keep only the last occurrence of each normalized package name.
- Return surviving original lines ordered by their last positions.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why would keeping the first occurrence violate the intended override behavior?

## Example Behavior

`dedupe_requirements(['A==1.0.0', 'b==1.0.0', 'a==2.0.0'])` → `['b==1.0.0', 'a==2.0.0']`.
