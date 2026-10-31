# Curriculum quality and release status

## What the automated audit establishes

The GitHub Actions workflow `.github/workflows/gauntlex-audit.yml` checks the task directory structure, JSON metadata, sequential numbering, prerequisites, Python syntax, and presence of pytest functions. Separate reference checks currently cover selected foundational, function, algorithm, and text/file contracts. A green run establishes only that these checks passed; it does **not** certify all tasks or their solutions.

## What remains unverified

- Most of the 409 tasks have not been exercised against independently written, correct reference implementations.
- Edge cases, error handling, CLI exit codes, and exact output contracts require manual review and additional tests.
- The 693 entries in `CURRICULUM_ORDER.md` are a source inventory, not 693 completed Gauntlex exercises.
- `gauntlex/source_traceability.json` is intentionally empty until individual source-to-task mappings have been reviewed. The mapping report must not be represented as confirmed source coverage.
- Starter files are intentionally incomplete. A failing student acceptance test is normal before the exercise is solved.

## Release checklist

1. Run `python scripts/audit_gauntlex.py` and the existing contract verification scripts.
2. Review every task's README, metadata, starter API, and acceptance tests as one contract.
3. Run each acceptance suite against an independent reference implementation; ensure the unfinished starter fails for the intended reason.
4. Add tests for malformed inputs, boundary cases, determinism, and security-relevant failure paths where appropriate.
5. Verify source provenance and licenses before importing source content; document each confirmed mapping.
6. Review the curriculum order for actual prerequisite dependencies and increasing complexity.
7. Keep authoritative tests private when integrating into the Gauntlex platform; learner-visible tests can be illustrative.

**Current designation:** draft curriculum; automated static checks and partial reference verification are in place. Not yet certified as a complete, source-covered, end-to-end tested Python Piscine.
