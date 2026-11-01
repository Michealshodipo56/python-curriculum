# Plan Log Backups

## Description
Generate a predictable sequence of backup filenames without changing the filesystem.

### Behavior contract
Given a base filename and positive number of backups, return backup filenames in ascending numeric order, from `.1` to `.N`. Do not touch the filesystem.

## Requirements
- Implement `rotation_names(base, backups)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Tips
This task plans names only; it does not rotate files.

The task defines behavior; design the implementation independently.
