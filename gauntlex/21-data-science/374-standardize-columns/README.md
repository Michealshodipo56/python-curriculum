# standardize_columns

## Challenge
Given a rectangular matrix of numeric rows, standardize each column independently using population mean and standard deviation. Constant columns become zeros. Return [] for empty matrix; raise ValueError for ragged rows.

## Requirements
- Implement `standardize_columns(matrix)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Compute column statistics, then transform each row.

## Run tests
`python -m pytest tests -q`
