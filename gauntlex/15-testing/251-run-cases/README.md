# Evaluate Examples

## Description

Turn a collection of expected input-output pairs into a simple test report. Each case should produce one boolean result.

## Requirements

- Implement `run_cases(fn, cases)` in `starter/solution.py`.
- Accept callable `fn` and cases shaped `[args, expected]`, where `args` is a list.
- Call `fn` with each case's positional arguments.
- Return booleans indicating whether the result equals the expected value, in case order.
- Allow exceptions from the callable to propagate.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips

- Why should the result list preserve the order of the cases?

## Example Behavior

For a function that doubles numbers, cases `[[[2], 4], [[3], 5]]` produce `[True, False]`.
