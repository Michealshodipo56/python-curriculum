# filter_suffix

## Challenge
Given a list of filenames and a suffix, return filenames whose final suffix matches case-insensitively, preserving order. The suffix must include the dot.

## Requirements
- Implement `filter_suffix(names, suffix)` in `starter/solution.py`.
- Use the Python standard library only.
- Return the specified result without printing.
- Do not mutate caller-owned values or touch files outside the specified paths.

## Hints
Compare lowercase suffixes rather than searching anywhere in the filename.

## Run tests
`python -m pytest tests -q`
