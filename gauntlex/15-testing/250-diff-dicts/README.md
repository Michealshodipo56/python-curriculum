# Compare Records

## Description
Identify missing and changed fields between two mappings.

### Behavior contract
Return a dictionary mapping keys with missing or unequal values to [old,new], using None for absent keys. Assume values are never None. Include keys from either mapping.

## Requirements
- Implement `diff_dicts(old, new)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
A missing key is not the same as an unchanged value.

Work from the contract and edge cases; do not include a finished implementation.
