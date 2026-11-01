# Summarize Security Events

## Description
Group security events by severity and type without assuming a fixed list of categories.

### Behavior contract
Given a list of event dictionaries containing `type` and `severity` strings, return counts grouped by severity: mapping severity to mapping type to integer count. Preserve all categories, including unknown strings.

## Requirements
- Implement `security_event_counts(events)` in `starter/solution.py`.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.
- Follow the specified security constraints rather than inventing cryptographic algorithms.

## Tips
Unknown categories are still valid data and should be counted.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.
