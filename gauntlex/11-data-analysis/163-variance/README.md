# Spread Around the Mean

## Description
Population variance measures how widely observations differ from their average. It uses squared deviations and divides by the number of observations.

## Requirements
- Implement `population_variance(values)` in `starter/solution.py`.
- Assume a nonempty list of numbers representing an entire population.
- Calculate the arithmetic mean and the average squared deviation from it.
- Use the population divisor `N`, not the sample divisor `N - 1`.
- Return the variance without modifying the data.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why are deviations squared rather than simply added?
- What happens when every value equals the mean?

## Example Behavior
`population_variance([1, 2, 3])` → `0.6666666666666666`

`population_variance([5, 5, 5])` → `0`
