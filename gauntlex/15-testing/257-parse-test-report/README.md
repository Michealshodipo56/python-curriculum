# Count Test Report Lines

## Description
Textual test reports often mix structured results with unrelated lines. Count only records that match a strict pass-or-fail format.

## Requirements
- Implement `parse_test_report(lines)` in `starter/solution.py`.
- Accept a sequence of lines.
- Count only lines matching `PASS name` or `FAIL name` with exactly one space and a nonempty name.
- Ignore all other lines, including malformed status lines.
- Return `{'passed': N, 'failed': M}` with both keys present.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is checking only the start of a line insufficient?

## Example Behavior
`parse_test_report(['PASS alpha', 'FAIL beta', 'PASS  extra', 'noise'])` → `{'passed': 1, 'failed': 1}`.
