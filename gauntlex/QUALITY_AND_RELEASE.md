# Curriculum verification and release criteria

## Two distinct inventories

- `CURRICULUM_ORDER.md` is the source-derived ordering of **693 assigned source activities** from four curricula, with nine source items withheld or merged. It is an ordering/index, not 693 fully packaged Gauntlex assignments.
- `gauntlex/` currently contains **409 separately authored Gauntlex tasks**. The count is not a coverage percentage: some Gauntlex tasks combine several concepts, and others are original extensions. No one-to-one mapping has been verified.

Do **not** claim that all 693 source activities have been converted, nor that 409 tasks are ready for production.

## Automated checks

Run `python scripts/audit_gauntlex.py` to validate directory structure, task metadata, sequence, prerequisite references and Python parseability. This audit has passed in GitHub Actions as of 2026-10-30. The audit does not prove runtime behavior, test correctness, pedagogy, source license compliance, or security.

## Mandatory release gates

1. **Source traceability:** For every one of the 693 assigned source entries, record its Gauntlex task ID(s), explicit exclusion with rationale, or an unimplemented status. Preserve original source paths and licensing/attribution information.
2. **Reference implementations:** Implement independent, private reference solutions. Run every test suite against the corresponding reference solution; a passing static audit is insufficient.
3. **Negative testing:** Confirm the intentionally incomplete starter fails appropriately. Test malformed input, empty data, boundary values, persistence, security constraints, and time/space complexity where specified.
4. **Manual pedagogy review:** Confirm each prerequisite is genuinely required, task difficulty increases coherently, and the Guide/Auditor prompts assess understanding without leaking solutions.
5. **Gauntlex integration:** Confirm runner entrypoints, working directories, subprocess timeouts, test isolation, grading output, and safe handling of untrusted code.
6. **Provenance and licensing:** Verify each source's license and redistribution permissions, and preserve required attribution. Original Gauntlex wording alone is not proof that all source material may be redistributed.

## Current release decision

**Not production ready.** Static validation is passing; behavioral verification, traceability, licensing review, and platform integration remain open.

## Source traceability tooling

Run `python scripts/source_traceability.py` for a coverage summary, or add `--json` for a per-source activity report. The `gauntlex/source_traceability.json` file maps exact source paths to reviewed Gauntlex task IDs; it intentionally starts empty rather than inferring equivalence from similar titles. The `--strict` option fails until every assigned source activity has an explicit mapping. GitHub Actions runs the non-strict summary so that structural CI can pass while release readiness remains blocked.

**Source access limitation:** The four source roots are pinned Git submodules (gitlinks, mode `160000`), not ordinary tracked directories in this repository. GitHub's contents API cannot read their nested files through this repository path. A source-by-source content review must inspect each pinned upstream submodule revision (for example by checking out the submodules), not rely solely on the index's titles. No source mapping has been certified yet.
