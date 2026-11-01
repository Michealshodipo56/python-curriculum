# Encode Categories

## Description
Represent category labels as vectors with a single active position.

### Behavior contract
Given a list of hashable labels and an ordered list of distinct classes, return a matrix of 0/1 rows with one 1 at each label's class position. Raise ValueError for unknown labels or duplicate classes.

## Requirements
- Implement `one_hot_encode(labels, classes)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
The class ordering defines which position each label occupies.

Reason about edge cases before designing your implementation.
