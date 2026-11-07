# Standard Spread

## Description
Population standard deviation describes the spread of values in the original units of the dataset rather than squared units.

## Requirements
- Implement `population_stddev(values)` in `starter/solution.py`.
- Assume a nonempty list of numeric observations.
- Return the square root of the population variance.
- Use the population divisor `N` for variance, not `N - 1`.
- Return zero when all values are equal; do not mutate the input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How is standard deviation related to variance?
- Why does taking a square root change the units?

## Example Behavior
`population_stddev([1, 1, 1])` → `0`

`population_stddev([3, 4, 5])` → `0.816496580927726`
