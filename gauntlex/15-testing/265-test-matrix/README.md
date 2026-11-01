# Cross-Platform Failures

## Description
Find tests that failed on at least one execution platform.

### Behavior contract
Given mapping of platform->mapping of test_name->bool, return sorted test names that failed on at least one platform.

## Requirements
- Implement `test_matrix(results)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
One failing platform is enough for a test to appear in the result.

Work from the contract and edge cases; do not include a finished implementation.
