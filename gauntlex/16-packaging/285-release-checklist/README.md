# release_checklist

## Challenge
Given booleans tests_passed, docs_updated, version_bumped, return an ordered list of missing steps among `run tests`, `update docs`, `bump version`. Empty list means release-ready.

## Requirements
- Implement `release_checklist(tests_passed, docs_updated, version_bumped)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Hints
Check each prerequisite in the specified order.

## Run tests
`python -m pytest tests -q`
