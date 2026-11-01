# Spread Around the Mean

## Description
Measure the average squared deviation of a population from its mean.

### Behavior contract
Return the population variance of a nonempty list of numbers (divide squared deviations by N).

## Requirements
- Implement `population_variance(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`population_variance([1, 2, 3])` → `0.6666666666666666`

`population_variance([5, 5, 5])` → `0`

## Tips
The word population matters: the divisor is the number of observations.

Examples illustrate expected values, not a solution.
