# release_notes

## Challenge
Given version and a list of change descriptions, return Markdown with first line `# Release VERSION`, a blank line, then one `- CHANGE` line per change. End with a newline. For no changes, return only heading and newline.

## Requirements
- Implement `release_notes(version, changes)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Build the heading and bullets separately so empty releases stay well formed.

## Run tests
`python -m pytest tests -q`
