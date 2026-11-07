# Expect a Failure

## Description

Some tests succeed only when a callable raises a particular exception. Validate the exception type and preserve the caught instance.

## Requirements

- Implement `assert_raises(expected_exception, fn)` in `starter/solution.py`.
- Call the zero-argument function `fn`.
- Return the caught exception when it is an instance of `expected_exception`.
- Raise `AssertionError` if `fn` returns normally or raises a different exception type.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why is a normal return a failure for this test?
- What distinguishes an exception instance from its class?

## Example Behavior

A callable raising `ValueError('bad')` passes when `ValueError` is expected and returns that exception instance.
