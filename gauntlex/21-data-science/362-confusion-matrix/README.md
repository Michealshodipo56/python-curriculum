# Classify the Outcomes

## Description
Binary classifiers can be evaluated by counting correct and incorrect predictions for positive and negative cases.

## Requirements
- Implement `confusion_matrix(actual, predicted)` in `starter/solution.py`.
- Require actual and predicted Boolean sequences of equal length.
- Return integer counts under keys `tp`, `tn`, `fp`, and `fn`.
- Classify each paired observation exactly once.
- Raise `ValueError` for length mismatch.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- What distinguishes a false positive from a false negative?

## Example Behavior
`confusion_matrix([True, False], [True, True])` → `{'tp': 1, 'tn': 0, 'fp': 1, 'fn': 0}`.
