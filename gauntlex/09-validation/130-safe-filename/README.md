# Safe File Labels

## Description

Turn a human-readable ASCII label into a predictable lowercase filename stem by replacing disallowed runs with underscores.

## Requirements

- Implement `safe_filename(text)` in `starter/solution.py`.
- Convert ASCII letters to lowercase.
- Keep lowercase `a`–`z`, digits `0`–`9`, underscores, and hyphens.
- Replace each run of other characters with one underscore.
- Remove leading and trailing underscores.
- Return `'untitled'` when no usable stem remains.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips

- Why should consecutive punctuation produce one separator?
- What happens when every input character is disallowed?

## Example Behavior

`safe_filename('My Report (2024)')` → `'my_report_2024'`; `safe_filename('!!!')` → `'untitled'`.
