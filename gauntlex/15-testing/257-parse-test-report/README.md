# parse_test_report

## Challenge
Given lines formatted `PASS name`, `FAIL name`, or other text, return counts as {'passed':N,'failed':M}, ignoring other lines. Require exactly one space between status and a nonempty name.

## Requirements
- Implement `parse_test_report(lines)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
Match the whole line, not just its prefix.

## Run tests
`python -m pytest tests -q`
