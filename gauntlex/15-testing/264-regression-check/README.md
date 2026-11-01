# Spot Regressions

## Description
Compare two sets of results to find tests that changed from passing to failing.

### Behavior contract
Given mappings test_name->bool for baseline and current runs, return sorted names that passed previously but fail now. Ignore tests absent from either run.

## Requirements
- Implement `regressions(baseline, current)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
Only compare tests present in both runs; newly introduced tests are not regressions.

Work from the contract and edge cases; do not include a finished implementation.
