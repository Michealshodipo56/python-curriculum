# Sliding Average

## Description
A moving average smooths a sequence by averaging every consecutive group of a fixed size. Each neighboring group overlaps the previous one.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Assume `k` is a positive integer.
- Return one arithmetic average for each contiguous window of `k` values.
- Preserve the left-to-right order of windows.
- Return `[]` if `k` exceeds the number of observations.
- Do not mutate the input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How many windows fit in a list of length `N`?
- What changes when the window moves one position?

## Example Behavior
`moving_average([1, 2, 3, 4], 2)` → `[1.5, 2.5, 3.5]`

`moving_average([1, 2], 3)` → `[]`
