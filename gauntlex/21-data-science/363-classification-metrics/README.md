# Measure a Classifier

## Description
Calculate precision, recall, accuracy, and F1 from classification outcome counts.

### Behavior contract
Given integer tp,tn,fp,fn >=0, return precision, recall, accuracy and f1 as floats in a dictionary. Use 0.0 when any metric denominator is zero, including accuracy on an empty sample. Raise ValueError for negative counts.

## Requirements
- Implement `classification_metrics(tp, tn, fp, fn)` in `starter/solution.py`.
- Use only Python's standard library; no NumPy, pandas, or scikit-learn.
- Return the specified values without printing or mutating input data.
- Floating-point answers are checked approximately where appropriate.

## Tips
Each metric answers a different question and has its own denominator.

Reason about edge cases before designing your implementation.
