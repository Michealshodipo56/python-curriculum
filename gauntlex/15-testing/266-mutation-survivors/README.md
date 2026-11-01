# Undetected Mutations

## Description
Identify modified implementations that none of the supplied tests rejected.

### Behavior contract
Given mapping of mutant_id->list of booleans indicating whether each test passed, return sorted mutant IDs for which all tests passed (including no tests).

## Requirements
- Implement `surviving_mutants(results)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
A mutation with no tests has not been detected.

Work from the contract and edge cases; do not include a finished implementation.
