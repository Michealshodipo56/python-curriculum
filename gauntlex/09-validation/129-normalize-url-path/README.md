# normalize_url_path

## Description
Normalize a POSIX URL path by collapsing repeated slashes and removing . segments. Resolve .. segments without going above root. Return a leading /; do not preserve trailing slash except root.

## Requirements
- Implement `normalize_url_path(path)` in `starter/solution.py`.
- Return the specified value; do not print or read from standard input.
- Do not mutate caller-owned collections.
- Use Python's standard library only.

## Examples
`normalize_url_path("/a//b/./c/../d")` → `"/a/b/d"`

`normalize_url_path("../../x")` → `"/x"`

## Tips
A stack can resolve path segments without accessing the filesystem.
