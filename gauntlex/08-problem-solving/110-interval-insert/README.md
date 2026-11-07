# Add a New Range

## Description

Insert one new closed interval into an already sorted, nonoverlapping collection, merging any ranges it overlaps or touches.

## Requirements

- Implement `insert_interval(intervals, new_interval)` in `starter/solution.py`.
- Assume `intervals` is sorted and contains nonoverlapping closed integer intervals.
- Insert `new_interval` in its correct position.
- Merge any overlapping or endpoint-touching ranges.
- Return sorted nonoverlapping intervals without modifying inputs.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips

- Which existing intervals lie completely before the new interval?
- How do overlapping ranges affect the new interval's boundaries?

## Example Behavior

`insert_interval([[1, 3], [6, 9]], [2, 5])` → `[[1, 5], [6, 9]]`; `insert_interval([], [2, 4])` → `[[2, 4]]`.
