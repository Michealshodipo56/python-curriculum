# Hold Out Examples

## Description
Model evaluation requires separating training and held-out observations. Preserve the original order instead of shuffling.

## Requirements
- Implement `train_test_split(items, test_fraction)` in `starter/solution.py`.
- Require `test_fraction` between `0` and `1` inclusive; otherwise raise `ValueError`.
- Use `floor(len(items) * test_fraction)` as the test count.
- Take test items from the end and return `[training_items, test_items]`.
- Preserve item order in both groups.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why does choosing the final observations matter for reproducibility?

## Example Behavior
`train_test_split([1, 2, 3, 4], 0.25)` → `[[1, 2, 3], [4]]`.
