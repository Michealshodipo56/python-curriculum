# Expect a Failure

## Description
Check that a callable raises the correct type of exception.

### Behavior contract
Call zero-argument fn and return the caught exception if it is an instance of expected_exception; otherwise raise AssertionError. If fn returns normally, raise AssertionError.

## Requirements
- Implement `assert_raises(expected_exception, fn)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Tips
A function that returns normally does not satisfy an expected-exception contract.

Work from the contract and edge cases; do not include a finished implementation.
