# rotation_names

## Challenge
Given a base filename and positive number of backups, return backup filenames in ascending numeric order, from `.1` to `.N`. Do not touch the filesystem.

## Requirements
- Implement `rotation_names(base, backups)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Validate the backup count before generating names.

## Run tests
`python -m pytest tests -q`
