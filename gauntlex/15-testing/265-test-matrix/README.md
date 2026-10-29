# test_matrix

## Challenge
Given mapping of platform->mapping of test_name->bool, return sorted test names that failed on at least one platform.

## Requirements
- Implement `test_matrix(results)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Union failing test names across platform results.

## Run tests
`python -m pytest tests -q`
