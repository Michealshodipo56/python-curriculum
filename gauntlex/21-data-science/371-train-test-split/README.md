# train_test_split

## Challenge
Given a sequence and a test_fraction in [0,1], return [training_items,test_items] with original order preserved. Test size is floor(len(items)*test_fraction); take test items from the end. Raise ValueError for invalid fractions.

## Requirements
- Implement `train_test_split(items, test_fraction)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Hint
Compute split size before slicing.

## Run tests
`python -m pytest tests -q`
