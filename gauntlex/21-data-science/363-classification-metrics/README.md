# Measure a Classifier

## Description
Different evaluation metrics capture different kinds of classification performance. Derive four measures from outcome counts.

## Requirements
- Implement `classification_metrics(tp, tn, fp, fn)` in `starter/solution.py`.
- Accept nonnegative integer `tp`, `tn`, `fp`, and `fn`; reject negative counts with `ValueError`.
- Return a dictionary containing floating-point `precision`, `recall`, `accuracy`, and `f1`.
- Use `0.0` whenever a metric's denominator is zero, including an empty sample.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why can precision and recall disagree for the same classifier?

## Example Behavior
`classification_metrics(1, 1, 0, 0)` → all four metrics equal `1.0`.
