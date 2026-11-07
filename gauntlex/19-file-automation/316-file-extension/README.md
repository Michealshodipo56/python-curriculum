# Recognize File Extensions

## Description
A file's final suffix can identify its type, but hidden files beginning with a dot need careful treatment.

## Requirements
- Implement `file_extension(filename)` in `starter/solution.py`.
- Return the lowercase final extension, including its leading dot.
- Do not count the leading dot of a dotfile as an extension by itself.
- Return `''` when there is no extension.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- How does `.env` differ from `.env.local`?

## Example Behavior
`file_extension('REPORT.CSV')` → `'.csv'`; `file_extension('.env')` → `''`.
