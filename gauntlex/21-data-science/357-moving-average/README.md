# Smooth with Windows

## Description
A moving average summarizes adjacent observations and smooths short-term fluctuations without changing their sequence.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Accept a sequence and positive integer window size `k`.
- Return floating-point averages for each consecutive window of exactly `k` observations.
- Return `[]` when `k` exceeds the sequence length.
- Raise `ValueError` when `k < 1`.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Generate a result only for each complete window of length `k`; preserve observation order. An oversized window produces no results, while a nonpositive size is invalid.

## Tips
- How does the next window differ from the previous window?

## Example Behavior
`moving_average([2, 4, 6, 8], 2)` → `[3.0, 5.0, 7.0]`.
