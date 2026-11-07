# Wheel Filename

## Description

A Python wheel filename encodes the distribution, version, and compatibility tags. Assemble the expected filename from trusted components.

## Requirements

- Implement `wheel_name(name, version, python_tag)` in `starter/solution.py`.
- Accept trusted, nonempty package name, version, and Python tag strings.
- Convert hyphens in the package name to underscores.
- Return `NAME-VERSION-TAG-none-any.whl` using the converted name.
- Do not alter the version or Python tag.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why is the distribution name represented differently inside a wheel filename?

## Example Behavior

`wheel_name('my-package', '1.2.0', 'py3')` → `'my_package-1.2.0-py3-none-any.whl'`.
