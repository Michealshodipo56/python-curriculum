# Standard Spread

## Description
Measure the typical spread of population values in the original units of the data.

### Behavior contract
Return the population standard deviation of a nonempty list of numbers.

## Requirements
- Implement `population_stddev(values)` in `starter/solution.py`.
- Return the result; do not print or read standard input.
- Do not mutate the input lists.
- Use only the Python standard library.

## Examples
`population_stddev([1, 1, 1])` → `0`

`population_stddev([3, 4, 5])` → `0.816496580927726`

## Tips
Consider why taking the square root changes the units of variance.

Examples illustrate expected values, not a solution.
