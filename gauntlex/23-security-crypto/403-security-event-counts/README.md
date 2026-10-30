# security_event_counts

## Challenge
Given a list of event dictionaries containing `type` and `severity` strings, return counts grouped by severity: mapping severity to mapping type to integer count. Preserve all categories, including unknown strings.

## Requirements
- Implement `security_event_counts(events)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Hint
Build nested counters without assuming fixed severity values.

## Run tests
`python -m pytest tests -q`
