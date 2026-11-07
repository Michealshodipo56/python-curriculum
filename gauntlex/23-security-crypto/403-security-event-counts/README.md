# Summarize Security Events

## Description

Group security events by severity and type without assuming a fixed list of categories.

## Requirements

- Implement `security_event_counts(events)` in `starter/solution.py`.
- Given a list of event dictionaries containing `type` and `severity` strings, return counts grouped by severity: mapping severity to mapping type to integer count. Preserve all categories, including unknown strings.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations

Count every severity/type combination without relying on a fixed vocabulary. Unknown category strings are legitimate data and must remain in the nested result.

## Tips

Unknown categories are still valid data and should be counted.

## Example Behavior

`security_event_counts([{'severity': 'high', 'type': 'login'}, {'severity': 'high', 'type': 'login'}])` → `{'high': {'login': 2}}`.
