# Canonical URL Paths

## Description
Resolve redundant separators and relative segments to produce a stable rooted URL path.

### Behavior contract
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
Treat parent segments at the root carefully: normalization must never travel above it.

The examples specify results without giving an implementation.
