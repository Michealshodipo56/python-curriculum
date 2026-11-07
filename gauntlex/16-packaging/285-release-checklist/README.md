# Release Readiness

## Description

A release should proceed only when its required checks are complete. Report missing steps in a consistent order.

## Requirements

- Implement `release_checklist(tests_passed, docs_updated, version_bumped)` in `starter/solution.py`.
- Accept booleans `tests_passed`, `docs_updated`, and `version_bumped`.
- For each false condition, include its corresponding action: `run tests`, `update docs`, or `bump version`.
- Return missing actions in that exact order.
- Return `[]` when every condition is true.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips

- Why is a fixed checklist order useful for repeatable release reviews?

## Example Behavior

`release_checklist(False, True, False)` → `['run tests', 'bump version']`; all true → `[]`.
