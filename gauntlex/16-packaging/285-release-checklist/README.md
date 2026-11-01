# Release Readiness

## Description
Report which release prerequisites are still missing in a fixed order.

### Behavior contract
Given booleans tests_passed, docs_updated, version_bumped, return an ordered list of missing steps among `run tests`, `update docs`, `bump version`. Empty list means release-ready.

## Requirements
- Implement `release_checklist(tests_passed, docs_updated, version_bumped)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
A release is ready only when every required condition is satisfied.

The learner must develop the implementation from the stated contract.
