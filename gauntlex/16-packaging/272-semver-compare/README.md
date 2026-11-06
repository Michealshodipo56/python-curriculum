# Version Ordering

## Description
Version components represent numeric precedence, not ordinary string order. Compare major, minor, and patch numbers in significance order.

## Requirements
- Implement `compare_version(a, b)` in `starter/solution.py`.
- Accept two valid three-part versions without prerelease or build suffixes.
- Return `-1` if the first version is older, `0` if equal, and `1` if newer.
- Compare components numerically in major, minor, then patch order.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why does `1.10.0` come after `1.9.0`?

## Example Behavior
`compare_version('1.9.0', '1.10.0')` → `-1`; `compare_version('2.0.0', '2.0.0')` → `0`.
