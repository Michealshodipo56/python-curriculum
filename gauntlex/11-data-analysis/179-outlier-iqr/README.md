# Outside the Fences

## Description

The interquartile range describes the spread of the middle half of a dataset. Use it to identify observations beyond the standard lower and upper fences.

## Requirements

- Implement `iqr_outliers(values)` in `starter/solution.py`.
- Return `[]` for fewer than four values.
- Determine `Q1` and `Q3` as medians of the lower and upper halves of sorted data.
- For odd-length datasets, exclude the overall median from both halves.
- Define `IQR = Q3 - Q1` and fences at `Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`.
- Return only values strictly outside those fences, preserving original input order.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips

- Why does the quartile definition matter for odd-sized datasets?
- Why are values exactly on a fence not outliers?

## Example Behavior

`iqr_outliers([1, 2, 2, 3, 3, 4, 5, 6, 100])` → `[100]`

`iqr_outliers([1, 2, 3])` → `[]`
