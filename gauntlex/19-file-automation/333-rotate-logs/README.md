# Plan Log Backups

## Description
Log rotation can be planned as a deterministic sequence of backup names. This exercise generates names without performing filesystem operations.

## Requirements
- Implement `rotation_names(base, backups)` in `starter/solution.py`.
- Accept a base filename and a positive backup count.
- Return filenames formed by appending `.1` through `.N` to the base.
- Keep the names in ascending numeric order.
- Do not create, rename, or delete files.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why is separating a rotation plan from actual file operations useful?

## Example Behavior
`rotation_names('app.log', 3)` → `['app.log.1', 'app.log.2', 'app.log.3']`.
