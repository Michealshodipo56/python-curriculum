# root_mean_square_error

## Challenge
Return square root of average squared prediction error for equal-length nonempty sequences. Raise ValueError for mismatched or empty inputs.

## Requirements
- Implement `root_mean_square_error(actual, predicted)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Square each error before averaging.

## Run tests
`python -m pytest tests -q`
