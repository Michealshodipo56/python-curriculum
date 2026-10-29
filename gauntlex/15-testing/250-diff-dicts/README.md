# diff_dicts

## Challenge
Return a dictionary mapping keys with missing or unequal values to [old,new], using None for absent keys. Assume values are never None. Include keys from either mapping.

## Requirements
- Implement `diff_dicts(old, new)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Take the union of keys and compare their associated values.

## Run tests
`python -m pytest tests -q`
