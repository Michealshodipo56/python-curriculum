# Interpret a Boolean

## Description

A configuration value may express yes or no using several text forms. Convert recognized forms to Boolean values and reject unsupported tokens.

## Requirements

- Implement `parse_boolean(text)` in `starter/solution.py`.
- Ignore surrounding whitespace and letter case.
- Return `True` for `true`, `yes`, or `1`.
- Return `False` for `false`, `no`, or `0`.
- Raise `ValueError` for every other string, including an empty value.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why should an unknown token not silently become `False`?
- Consider uppercase words and spaces around input.

## Example Behavior

`parse_boolean(' YES ')` → `True`; `parse_boolean('No')` → `False`; `parse_boolean('maybe')` raises `ValueError`.
