# Where Ranges Overlap

## Description
Find the shared portions of two ordered collections of disjoint intervals.

### Behavior contract
Given two sorted lists of pairwise-disjoint inclusive integer intervals, return sorted pairwise intersections [start,end].

## Requirements
- Implement `interval_intersection(a, b)` in `starter/solution.py`.
- Use Python's standard library only.
- Do not mutate inputs or print.
- Respect the specified asymptotic complexity.

## Tips
Advancing the interval that ends first avoids unnecessary comparisons.

The task is to design an implementation that meets both behavior and efficiency requirements.
