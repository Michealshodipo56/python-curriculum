# Three Outcomes

## Description

Summarize a test run that can pass, fail, or skip individual cases. A complete report includes zero counts for absent outcomes.

## Requirements

- Implement `test_summary(records)` in `starter/solution.py`.
- Accept dictionaries containing a `status` of `pass`, `fail`, or `skip`.
- Count records for each status and the total number of records.
- Return a dictionary with counts for all three statuses and `total`, even when some counts are zero.
- Return all zero counts for empty input.
- Use Python's standard library only; do not print or mutate inputs.

## Tips

- Why are explicit zero counts useful for reporting?

## Example Behavior

One pass and one skip produce counts `pass: 1`, `fail: 0`, `skip: 1`, and `total: 2`.
