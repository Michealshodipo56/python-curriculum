# Scale to Zero and One

## Description
Different numeric ranges make features difficult to compare. Rescale observations using the dataset minimum and maximum while preserving their order.

## Requirements
- Implement `min_max_scale(values)` in `starter/solution.py`.
- Map each value to `(value - minimum) / (maximum - minimum)`.
- Return `[]` for empty input.
- If all values are equal, return one zero per value.
- Do not modify the original sequence.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Tips
- Why does a constant dataset need special handling?

## Example Behavior
`min_max_scale([2, 4, 6])` → `[0.0, 0.5, 1.0]`.
