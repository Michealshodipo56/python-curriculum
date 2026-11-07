# Gauntlex Python Curriculum — Documentation Audit

Review date: **2026-11-07**. Scope: the current `python-curriculum` checkout, following the completed merge at `01bd7e9`.

## Outcome and scope

All **409 numbered challenges across 23 sections** are accounted for. Every challenge README was inspected alongside its starter interface and existing test contract. Existing local specification/verification utilities and source-review notes were consulted where available. The audit preserves challenge IDs, directory locations, public starter signatures, existing tests, metadata, pinned sources, attribution, and licenses.

This is a documentation and ordering review. No learner implementation, new acceptance test, modified test, or Gauntlex platform integration was introduced. The only changed Python file is the existing Markdown publishing utility, so automatic publication retains the corrected order and heading hierarchy.

## Corrections

- Normalized heading spacing across all 409 READMEs and corrected starter paths in 035–062. Existing authored briefs were retained rather than replaced wholesale.
- Gave Section 06 an individual contract review, clarifying slug characters, valid input assumptions, CSV empty/invalid values, copy semantics, line boundaries, and relevant edge-case examples.
- Corrected malformed pipe-delimited log requirements, the RGB tuple examples, the undo return value, missing tested exception types, a count key/value type error, and the Dijkstra unreachable-node contradiction.
- Replaced placeholder examples for cache keys and request identifiers. Removed repeated generic tips from object and security exercises; repaired tips joined by template separators.
- Expanded the nine existing capstone requirement paragraphs into readable, verifiable contracts, preserving their original commands, storage interfaces, JSON shapes, and failure behavior.
- Synchronized titles and paths in the learner path and curriculum order. Preserved the complete historical 693-source-activity inventory as a clearly labeled appendix. Restored `UNIFIED_PYTHON_CURRICULUM.md` as a compatibility navigation document pointing to the maintained master.
- Regenerated the master with correctly nested section/challenge/subsection headings. The publishing utility now reproduces numeric order, including both project checkpoints.

## Progression decision

The documented sequence is **001–409 in numeric order**. Challenges 311–314 remain the core-project checkpoint before extension challenges 315–404; 405–409 form the final-project checkpoint. Previously, moving all capstones to the end of the index put 315 ahead of its explicit prerequisite 314. Correcting the navigation resolves that issue without changing metadata, renumbering, or moving directories.

Section 18 is represented at two checkpoints, but there are still exactly 23 distinct section directories. Every declared prerequisite resolves to an earlier challenge in the documented path. Section introductions explain new concepts and transitions, including functions after terminal programs, standard-library imports and file/error handling, classes before stateful objects, SQL before transactions, awaitables before async coordination, and the WSGI interface before middleware.

Difficulty rises within each topic, with introductory exercises at new topic boundaries and deliberate consolidation after projects. The course is a problem-first Python practice curriculum; the numeric sequence is not a claim that every adjacent task is harder than its predecessor or that every Python ecosystem library is taught.

## Overlap retained intentionally

| Challenges | Reason to retain |
|---|---|
| 043 / 062 | One-level flattening precedes recursive traversal. |
| 051 / 059 | Multiple delimiter types and a stack-like invariant versus parentheses-only balance practice. |
| 053 / 385 / 386 | Initial alphabet arithmetic, later security-context consolidation, and fixed self-inverse ROT13. |
| 072 / 316 | The earlier function omits the dot; the file-automation API includes it. |
| 078 / 323 | Basic text-file counting is deliberately revisited before the later file-automation projects. |
| 105 / 379 | The later brief adds an explicit linear-time target. |
| 108 / 381 | Numeric tie-breaking versus first-seen tie-breaking and generic hashable values. |
| 109 / 377 | Shared endpoints versus inclusive integer adjacency: `[1,2]` and `[3,4]` merge only in 377. |
| 123 / 397 | Canonical IPv4 validation is reinforced in the later security track. |
| 166 / 357 | The later exercise requires rejecting invalid window sizes. |
| 167 / 355 | Scaling is revisited as preparation for the later multifeature standardization task. |
| 169 / 367 | The later API explicitly rejects dimensional mismatch. |
| 176 / 359 | The earlier API returns None for zero total weight; the later validated API raises ValueError. |
| 193 / 404; 195 / 391 | Security primitives are deliberately rehearsed before the final projects. |
| 196 / 392 | Earlier lowercase-only signatures versus later acceptance of either hexadecimal case. |
| 200 / 300 / 334 | Related serialization/hash skills applied to cache identity, idempotency, and configuration. |

No duplicate README titles were found. No exercise was deleted merely for revisiting a concept.

## Verification evidence

- Existing `audit_gauntlex.py`: 409 packages, zero structural issues.
- Existing `audit_readme_contracts.py`: 409 briefs, zero missing required sections or detected starter-interface mismatches.
- Existing function API audit: all 12 function-section interfaces match the README and existing tests.
- All 409 metadata files and 818 challenge Python files were read statically; starter files remain intentionally incomplete.
- Compared 283 README examples sharing literal calls with existing test assertions: zero value or container-type mismatches after correction.
- Checked 2,384 local link occurrences, including authored navigation and source-inventory targets, source-inventory file targets, challenge counts and IDs, unique titles, prerequisite positions, Markdown fences and inline-code delimiters, master heading structure, and master regeneration consistency.
- All 693 primary paths in the preserved source inventory exist in the local source checkouts. This verifies local references, not equivalence of all source learning outcomes.
- Final diff scope is restricted to Markdown documentation and `tools/build_gauntlex_master.py`; challenge tests, starters, metadata, source gitlinks, and platform files are unchanged.

Existing learner test suites were **not executed**, because starter work is intentionally incomplete and this task does not authorize implementing solutions. The audit does not represent static checks as proof of full behavioral coverage. External HTTP links were not fetched; local links and authored navigation were checked without making network requests to example URLs.

## Outstanding issues requiring work outside documentation

1. **Challenge 051 reference-helper mismatch.** The pre-existing reference snippet in `scripts/verify_algorithm_contracts.py` assumes every non-opening character is a closing delimiter, while the README requires ignoring nonbracket characters. The supplied challenge tests contain bracket-only strings and do not establish that broader behavior. The intended README contract is retained; the helper and tests are untouched.
2. **Challenge 074 reference-helper format gap.** The pre-existing helper in `scripts/verify_text_file_contracts.py` uses a permissive ISO-date parser plus a length check. A ten-character ISO week-date string can pass that helper even though the assignment requires `YYYY-MM-DD`. Existing calendar-date examples do not exercise that distinction. The stated format remains authoritative; no implementation or test was changed.
3. **Limited acceptance coverage.** Many suites assert only a few examples. Some test only output, not complexity, concurrency cleanup, immutability, transaction ownership, path/symlink containment, or cryptographic primitive selection. Exact float equality in parts of Section 11 may also reject mathematically equivalent floating-point calculations with a different rounding order. Those checks need a separately authorized testing task; this audit adds none.
4. **Pre-existing test syntax warning.** The regular-expression string in `gauntlex/15-testing/270-assert-subset/tests/test_solution.py` contains an unrecognized escape and produces a SyntaxWarning under the local Python version. The test was not edited.
5. **Specification boundaries.** WSGI briefs define selected paths/methods rather than a complete HTTP service. Several final CLIs specify an environment-supplied database path but no fallback when that variable is absent. Unstated combinations remain outside the documented contract; a future specification decision should precede additional grading requirements.
6. **Source coverage and licensing.** `gauntlex/source_traceability.json` is still empty; the current material does not establish a one-to-one mapping between 693 source activities and 409 authored challenges. Historical source-review statements are retained as historical records, not new certification. Source roots and license files are unchanged. Complete source-outcome mapping and redistribution review remain separate work.
7. **Future platform release.** Runtime integration, reference validation, runner isolation, and production grading are outside this documentation task. See [release criteria](gauntlex/QUALITY_AND_RELEASE.md). The curriculum has not been installed into the Gauntlex platform by this audit.

## Section inventory

| Section | IDs | Count |
|---|---|---|
| 01-foundations | 001–013 | 13 |
| 02-control-flow | 014–022 | 9 |
| 03-collections | 023–034 | 12 |
| 04-functions | 035–046 | 12 |
| 05-algorithms | 047–062 | 16 |
| 06-text-files | 063–080 | 18 |
| 07-objects | 081–095 | 15 |
| 08-problem-solving | 096–115 | 20 |
| 09-validation | 116–140 | 25 |
| 10-cli-tools | 141–160 | 20 |
| 11-data-analysis | 161–180 | 20 |
| 12-http-security | 181–205 | 25 |
| 13-sqlite | 206–230 | 25 |
| 14-async | 231–245 | 15 |
| 15-testing | 246–270 | 25 |
| 16-packaging | 271–285 | 15 |
| 17-architecture | 286–310 | 25 |
| 18-capstones | 311–314, 405–409 | 9 |
| 19-file-automation | 315–334 | 20 |
| 20-wsgi-web | 335–354 | 20 |
| 21-data-science | 355–374 | 20 |
| 22-advanced-algorithms | 375–384 | 10 |
| 23-security-crypto | 385–404 | 20 |

**Total: 409 challenges in 23 section directories.**

## Per-challenge review ledger

Every row records README, starter-interface, and existing-test-contract inspection. “Retained” means the authored requirements were kept; common Markdown spacing and index synchronization still apply. Source-equivalence certification is excluded from this ledger.

| ID | Existing challenge title | Review result |
|---|---|---|
| 001 | [First Signal](gauntlex/01-foundations/001-hello/README.md) | Reviewed; authored contract retained. |
| 002 | [The Answer](gauntlex/01-foundations/002-displaynumber/README.md) | Reviewed; authored contract retained. |
| 003 | [Two Signals](gauntlex/01-foundations/003-two-lines/README.md) | Reviewed; authored contract retained. |
| 004 | [Combine Values](gauntlex/01-foundations/004-addition/README.md) | Reviewed; authored contract retained. |
| 005 | [A Personal Greeting](gauntlex/01-foundations/005-greeting/README.md) | Reviewed; authored contract retained. |
| 006 | [Identity Card](gauntlex/01-foundations/006-name-card/README.md) | Reviewed; authored contract retained. |
| 007 | [Measure a Rectangle](gauntlex/01-foundations/007-rectangle/README.md) | Reviewed; authored contract retained. |
| 008 | [Share Into Groups](gauntlex/01-foundations/008-remainder/README.md) | Reviewed; authored contract retained. |
| 009 | [Name Initials](gauntlex/01-foundations/009-initials/README.md) | Reviewed; authored contract retained. |
| 010 | [Clean Announcement](gauntlex/01-foundations/010-shout/README.md) | Reviewed; authored contract retained. |
| 011 | [One Year Later](gauntlex/01-foundations/011-next-year/README.md) | Reviewed; authored contract retained. |
| 012 | [Even or Odd](gauntlex/01-foundations/012-even-or-odd/README.md) | Reviewed; authored contract retained. |
| 013 | [Choose the Larger](gauntlex/01-foundations/013-larger/README.md) | Reviewed; authored contract retained. |
| 014 | [Score Boundaries](gauntlex/02-control-flow/014-grade/README.md) | Reviewed; authored contract retained. |
| 015 | [Permission Gate](gauntlex/02-control-flow/015-access/README.md) | Reviewed; authored contract retained. |
| 016 | [Count Forward](gauntlex/02-control-flow/016-count/README.md) | Reviewed; authored contract retained. |
| 017 | [Running Total](gauntlex/02-control-flow/017-sum-range/README.md) | Reviewed; authored contract retained. |
| 018 | [Launch Countdown](gauntlex/02-control-flow/018-countdown/README.md) | Reviewed; authored contract retained. |
| 019 | [Even Accumulator](gauntlex/02-control-flow/019-even-sum/README.md) | Reviewed; authored contract retained. |
| 020 | [Times Table](gauntlex/02-control-flow/020-multiplication-table/README.md) | Reviewed; authored contract retained. |
| 021 | [Decimal Length](gauntlex/02-control-flow/021-digit-count/README.md) | Reviewed; authored contract retained. |
| 022 | [Find the Secret](gauntlex/02-control-flow/022-number-guess/README.md) | Reviewed; authored contract retained. |
| 023 | [Count the Collection](gauntlex/03-collections/023-list-length/README.md) | Reviewed; authored contract retained. |
| 024 | [At Both Ends](gauntlex/03-collections/024-list-ends/README.md) | Reviewed; authored contract retained. |
| 025 | [Sum the Collection](gauntlex/03-collections/025-list-total/README.md) | Reviewed; authored contract retained. |
| 026 | [Find the Peak](gauntlex/03-collections/026-list-maximum/README.md) | Reviewed; authored contract retained. |
| 027 | [Reverse the Sequence](gauntlex/03-collections/027-reverse-words/README.md) | Reviewed; authored contract retained. |
| 028 | [Keep the Evens](gauntlex/03-collections/028-filter-even/README.md) | Reviewed; authored contract retained. |
| 029 | [First Appearance](gauntlex/03-collections/029-unique-order/README.md) | Reviewed; authored contract retained. |
| 030 | [Word Tally](gauntlex/03-collections/030-word-frequency/README.md) | Reviewed; authored contract retained. |
| 031 | [Numeric Order](gauntlex/03-collections/031-sort-numbers/README.md) | Reviewed; authored contract retained. |
| 032 | [Inside the Boundaries](gauntlex/03-collections/032-middle-slice/README.md) | Reviewed; authored contract retained. |
| 033 | [Shared Vocabulary](gauntlex/03-collections/033-set-overlap/README.md) | Reviewed; authored contract retained. |
| 034 | [Matching Pairs](gauntlex/03-collections/034-pair-count/README.md) | Reviewed; authored contract retained. |
| 035 | [Return a Sum](gauntlex/04-functions/035-sum-function/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 036 | [Distance from Zero](gauntlex/04-functions/036-absolute-function/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 037 | [Factorial Product](gauntlex/04-functions/037-factorial/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 038 | [Mirror Text](gauntlex/04-functions/038-palindrome/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 039 | [Vowel Census](gauntlex/04-functions/039-vowel-count/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 040 | [Prime or Composite](gauntlex/04-functions/040-prime-check/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 041 | [Sequence Memory](gauntlex/04-functions/041-fibonacci/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 042 | [Same Letters, Different Order](gauntlex/04-functions/042-anagram/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 043 | [One Level Down](gauntlex/04-functions/043-flatten-once/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 044 | [First Unrepeated Character](gauntlex/04-functions/044-first-unique/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 045 | [Divide Into Chunks](gauntlex/04-functions/045-chunk-list/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 046 | [Greatest Shared Divisor](gauntlex/04-functions/046-gcd/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 047 | [Count the Words](gauntlex/05-algorithms/047-word-count/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 048 | [Longest in the Line](gauntlex/05-algorithms/048-longest-word/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 049 | [Circular Shift](gauntlex/05-algorithms/049-rotate-list/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 050 | [Two Ordered Streams](gauntlex/05-algorithms/050-merge-sorted/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 051 | [Nested Delimiters](gauntlex/05-algorithms/051-balanced-brackets/README.md) | Reviewed; authored contract retained. Starter path normalized. Pre-existing reference-helper issue recorded above. |
| 052 | [Compress Repeated Runs](gauntlex/05-algorithms/052-run-length/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 053 | [Alphabet Rotation](gauntlex/05-algorithms/053-caesar/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 054 | [Shared Beginning](gauntlex/05-algorithms/054-common-prefix/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 055 | [Rows Become Columns](gauntlex/05-algorithms/055-matrix-transpose/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 056 | [Halve the Search](gauntlex/05-algorithms/056-binary-search/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 057 | [Runner-Up Value](gauntlex/05-algorithms/057-second-largest/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 058 | [Group by Size](gauntlex/05-algorithms/058-group-by-length/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 059 | [Balance the Parentheses](gauntlex/05-algorithms/059-valid-parentheses/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 060 | [Zeros to the Back](gauntlex/05-algorithms/060-move-zeros/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 061 | [Build Pascal's Row](gauntlex/05-algorithms/061-pascal-row/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 062 | [Unfold Nested Lists](gauntlex/05-algorithms/062-flatten-recursive/README.md) | Reviewed; authored contract retained. Starter path normalized. |
| 063 | [One Space Apart](gauntlex/06-text-files/063-normalize-spaces/README.md) | Reviewed; authored contract retained. |
| 064 | [Count the Lines](gauntlex/06-text-files/064-line-count/README.md) | Added blank-line and empty-string examples. |
| 065 | [Parse With Care](gauntlex/06-text-files/065-safe-integer/README.md) | Reviewed; authored contract retained. |
| 066 | [Numbers Hidden in Text](gauntlex/06-text-files/066-extract-numbers/README.md) | Reviewed; authored contract retained. |
| 067 | [Protect the Address](gauntlex/06-text-files/067-mask-email/README.md) | Defined valid-address input assumptions. |
| 068 | [URL-Friendly Words](gauntlex/06-text-files/068-slugify/README.md) | Specified ASCII slug content and empty-slug behavior. |
| 069 | [Fields and Quotes](gauntlex/06-text-files/069-csv-row/README.md) | Specified well-formed CSV input, field whitespace, and empty fields. |
| 070 | [Find a JSON Field](gauntlex/06-text-files/070-json-value/README.md) | Specified the JSON-object input assumption. |
| 071 | [Compact JSON Text](gauntlex/06-text-files/071-json-compact/README.md) | Renamed compact JSON to avoid implying a formal canonicalization standard; clarified encoding. |
| 072 | [Final File Suffix](gauntlex/06-text-files/072-path-extension/README.md) | Added dotfile and missing-extension examples. |
| 073 | [Division Without Failure](gauntlex/06-text-files/073-safe-divide/README.md) | Reviewed; authored contract retained. |
| 074 | [Real Calendar Dates](gauntlex/06-text-files/074-parse-date/README.md) | Made the stated calendar format precise; reference-helper limitation recorded below. |
| 075 | [Calendar Distance](gauntlex/06-text-files/075-days-between/README.md) | Reviewed; authored contract retained. |
| 076 | [Day of the Week](gauntlex/06-text-files/076-iso-weekday/README.md) | Reviewed; authored contract retained. |
| 077 | [Keep Valid Records](gauntlex/06-text-files/077-clean-records/README.md) | Clarified non-string names and shallow copies, with an edge-case example. |
| 078 | [Read the Line Count](gauntlex/06-text-files/078-count-file-lines/README.md) | Connected file line counting to challenge 064. |
| 079 | [Load Structured Data](gauntlex/06-text-files/079-read-json-file/README.md) | Specified readable-file and valid-JSON assumptions. |
| 080 | [Sum a CSV Column](gauntlex/06-text-files/080-csv-column-total/README.md) | Clarified invalid-cell skipping, existing-column assumption, negative values, and empty totals. |
| 081 | [Last In, First Out](gauntlex/07-objects/081-stack/README.md) | Reviewed; authored contract retained. |
| 082 | [First In, First Out](gauntlex/07-objects/082-queue/README.md) | Reviewed; authored contract retained. |
| 083 | [Count by Key](gauntlex/07-objects/083-counter/README.md) | Reviewed; authored contract retained. |
| 084 | [Guard the Balance](gauntlex/07-objects/084-bank-account/README.md) | Reviewed; authored contract retained. |
| 085 | [Two Scales, One Value](gauntlex/07-objects/085-temperature/README.md) | Reviewed; authored contract retained. |
| 086 | [Shape Invariants](gauntlex/07-objects/086-rectangle-class/README.md) | Reviewed; authored contract retained. |
| 087 | [Track the Work](gauntlex/07-objects/087-todo-list/README.md) | Documented stored-title trimming. |
| 088 | [Immutable Coordinates](gauntlex/07-objects/088-point/README.md) | Reviewed; authored contract retained. |
| 089 | [Stock Ledger](gauntlex/07-objects/089-inventory/README.md) | Reviewed; authored contract retained. |
| 090 | [Student Averages](gauntlex/07-objects/090-gradebook/README.md) | Named the tested out-of-range exception. |
| 091 | [Publish and Listen](gauntlex/07-objects/091-event-emitter/README.md) | Reviewed; authored contract retained. |
| 092 | [Remember the Recent](gauntlex/07-objects/092-lru-cache/README.md) | Named the tested capacity exception. |
| 093 | [Step Back in Time](gauntlex/07-objects/093-undo-history/README.md) | Documented the undo return value. |
| 094 | [Cart Rules](gauntlex/07-objects/094-shopping-cart/README.md) | Reviewed; authored contract retained. |
| 095 | [Serve by Priority](gauntlex/07-objects/095-task-priority/README.md) | Reviewed; authored contract retained. |
| 096 | [Find the Pair](gauntlex/08-problem-solving/096-two-sum/README.md) | Reviewed; authored contract retained. |
| 097 | [Totals Along the Way](gauntlex/08-problem-solving/097-prefix-sums/README.md) | Reviewed; authored contract retained. |
| 098 | [Best Continuous Segment](gauntlex/08-problem-solving/098-max-subarray/README.md) | Reviewed; authored contract retained. |
| 099 | [Everyone Else's Product](gauntlex/08-problem-solving/099-product-except-self/README.md) | Reviewed; authored contract retained. |
| 100 | [Quarter Turn](gauntlex/08-problem-solving/100-rotate-matrix/README.md) | Reviewed; authored contract retained. |
| 101 | [Walk the Spiral](gauntlex/08-problem-solving/101-spiral-order/README.md) | Reviewed; authored contract retained. |
| 102 | [Write in Base Two](gauntlex/08-problem-solving/102-binary-conversion/README.md) | Reviewed; authored contract retained. |
| 103 | [Number to Numeral](gauntlex/08-problem-solving/103-roman-numerals/README.md) | Reviewed; authored contract retained. |
| 104 | [Numeral to Number](gauntlex/08-problem-solving/104-roman-to-int/README.md) | Reviewed; authored contract retained. |
| 105 | [Longest Without Repeats](gauntlex/08-problem-solving/105-longest-unique-substring/README.md) | Reviewed; authored contract retained. |
| 106 | [Smallest Sufficient Window](gauntlex/08-problem-solving/106-min-window-sum/README.md) | Reviewed; authored contract retained. |
| 107 | [Families of Letters](gauntlex/08-problem-solving/107-group-anagrams/README.md) | Reviewed; authored contract retained. |
| 108 | [Most Common Values](gauntlex/08-problem-solving/108-top-k-frequent/README.md) | Reviewed; authored contract retained. |
| 109 | [Unify Time Ranges](gauntlex/08-problem-solving/109-interval-merge/README.md) | Reviewed; authored contract retained. |
| 110 | [Add a New Range](gauntlex/08-problem-solving/110-interval-insert/README.md) | Reviewed; authored contract retained. |
| 111 | [Sudoku Constraints](gauntlex/08-problem-solving/111-valid-sudoku/README.md) | Reviewed; authored contract retained. |
| 112 | [Recolor a Region](gauntlex/08-problem-solving/112-flood-fill/README.md) | Reviewed; authored contract retained. |
| 113 | [Count the Islands](gauntlex/08-problem-solving/113-islands/README.md) | Reviewed; authored contract retained. |
| 114 | [Shortest Route](gauntlex/08-problem-solving/114-bfs-shortest-path/README.md) | Reviewed; authored contract retained. |
| 115 | [Detect a Loop](gauntlex/08-problem-solving/115-cycle-detection/README.md) | Reviewed; authored contract retained. |
| 116 | [Distinct After Normalization](gauntlex/09-validation/116-dedupe-normalized/README.md) | Reviewed; authored contract retained. |
| 117 | [Interpret a Boolean](gauntlex/09-validation/117-parse-boolean/README.md) | Reviewed; authored contract retained. |
| 118 | [Stay Within Bounds](gauntlex/09-validation/118-clamp/README.md) | Reviewed; authored contract retained. |
| 119 | [Telephone Canonical Form](gauntlex/09-validation/119-normalize-phone/README.md) | Reviewed; authored contract retained. |
| 120 | [Password Rules](gauntlex/09-validation/120-validate-password/README.md) | Reviewed; authored contract retained. |
| 121 | [Read URL Parameters](gauntlex/09-validation/121-parse-query/README.md) | Reviewed; authored contract retained. |
| 122 | [Write URL Parameters](gauntlex/09-validation/122-build-query/README.md) | Reviewed; authored contract retained. |
| 123 | [Four Network Octets](gauntlex/09-validation/123-validate-ipv4/README.md) | Reviewed; authored contract retained. |
| 124 | [Structured Log Entry](gauntlex/09-validation/124-parse-log-line/README.md) | Repaired broken log delimiters. |
| 125 | [Log Severity Summary](gauntlex/09-validation/125-count-log-levels/README.md) | Repaired broken log delimiters. |
| 126 | [Text Segments](gauntlex/09-validation/126-chunk-text/README.md) | Reviewed; authored contract retained. |
| 127 | [Configuration Assignments](gauntlex/09-validation/127-parse-env/README.md) | Reviewed; authored contract retained. |
| 128 | [Hide Sensitive Tokens](gauntlex/09-validation/128-redact-secrets/README.md) | Reviewed; authored contract retained. |
| 129 | [Canonical URL Paths](gauntlex/09-validation/129-normalize-url-path/README.md) | Reviewed; authored contract retained. |
| 130 | [Safe File Labels](gauntlex/09-validation/130-safe-filename/README.md) | Reviewed; authored contract retained. |
| 131 | [Clock Text to Seconds](gauntlex/09-validation/131-parse-duration/README.md) | Reviewed; authored contract retained. |
| 132 | [Seconds to Clock Text](gauntlex/09-validation/132-format-duration/README.md) | Reviewed; authored contract retained. |
| 133 | [Decode an RGB Color](gauntlex/09-validation/133-parse-hex-color/README.md) | Corrected RGB return type and examples to tuples. |
| 134 | [Encode an RGB Color](gauntlex/09-validation/134-format-hex-color/README.md) | Reviewed; authored contract retained. |
| 135 | [Clean the Tags](gauntlex/09-validation/135-normalize-tags/README.md) | Reviewed; authored contract retained. |
| 136 | [Domain Extraction](gauntlex/09-validation/136-email-domain/README.md) | Reviewed; authored contract retained. |
| 137 | [Shared Dictionary Keys](gauntlex/09-validation/137-common-keys/README.md) | Reviewed; authored contract retained. |
| 138 | [Reverse a Relationship](gauntlex/09-validation/138-invert-mapping/README.md) | Reviewed; authored contract retained. |
| 139 | [What Changed?](gauntlex/09-validation/139-diff-sets/README.md) | Reviewed; authored contract retained. |
| 140 | [Word Leaderboard](gauntlex/09-validation/140-top-words/README.md) | Reviewed; authored contract retained. |
| 141 | [Reverse the Stream](gauntlex/10-cli-tools/141-echo-lines/README.md) | Reviewed; authored contract retained. |
| 142 | [Line Numbers](gauntlex/10-cli-tools/142-number-lines/README.md) | Reviewed; authored contract retained. |
| 143 | [Find Matching Lines](gauntlex/10-cli-tools/143-grep-literal/README.md) | Reviewed; authored contract retained. |
| 144 | [First Lines Only](gauntlex/10-cli-tools/144-head-lines/README.md) | Reviewed; authored contract retained. |
| 145 | [Last Lines Only](gauntlex/10-cli-tools/145-tail-lines/README.md) | Reviewed; authored contract retained. |
| 146 | [Order the Lines](gauntlex/10-cli-tools/146-sort-lines/README.md) | Reviewed; authored contract retained. |
| 147 | [Collapse Repeated Lines](gauntlex/10-cli-tools/147-unique-adjacent/README.md) | Reviewed; authored contract retained. |
| 148 | [Count Matching Lines](gauntlex/10-cli-tools/148-count-occurrences/README.md) | Reviewed; authored contract retained. |
| 149 | [Sum the Stream](gauntlex/10-cli-tools/149-sum-columns/README.md) | Reviewed; authored contract retained. |
| 150 | [CSV to Tabs](gauntlex/10-cli-tools/150-csv-to-tsv/README.md) | Reviewed; authored contract retained. |
| 151 | [Readable JSON](gauntlex/10-cli-tools/151-json-pretty/README.md) | Reviewed; authored contract retained. |
| 152 | [Compact JSON Stream](gauntlex/10-cli-tools/152-json-lines/README.md) | Reviewed; authored contract retained. |
| 153 | [Count Active Records](gauntlex/10-cli-tools/153-jsonl-count/README.md) | Reviewed; authored contract retained. |
| 154 | [Extract JSON Fields](gauntlex/10-cli-tools/154-jsonl-select/README.md) | Reviewed; authored contract retained. |
| 155 | [Count CSV Records](gauntlex/10-cli-tools/155-csv-row-count/README.md) | Reviewed; authored contract retained. |
| 156 | [Extract a CSV Column](gauntlex/10-cli-tools/156-csv-select-column/README.md) | Reviewed; authored contract retained. |
| 157 | [Filter CSV Records](gauntlex/10-cli-tools/157-csv-filter-equal/README.md) | Reviewed; authored contract retained. |
| 158 | [Three Text Measures](gauntlex/10-cli-tools/158-word-count-cli/README.md) | Reviewed; authored contract retained. |
| 159 | [Value Histogram](gauntlex/10-cli-tools/159-histogram/README.md) | Reviewed; authored contract retained. |
| 160 | [Numeric Stream Summary](gauntlex/10-cli-tools/160-stats-cli/README.md) | Reviewed; authored contract retained. |
| 161 | [The Middle Value](gauntlex/11-data-analysis/161-median/README.md) | Reviewed; authored contract retained. |
| 162 | [Most Frequent Observation](gauntlex/11-data-analysis/162-mode/README.md) | Reviewed; authored contract retained. |
| 163 | [Spread Around the Mean](gauntlex/11-data-analysis/163-variance/README.md) | Reviewed; authored contract retained. |
| 164 | [Standard Spread](gauntlex/11-data-analysis/164-standard-deviation/README.md) | Reviewed; authored contract retained. |
| 165 | [Nearest-Rank Percentile](gauntlex/11-data-analysis/165-percentile-nearest/README.md) | Reviewed; authored contract retained. |
| 166 | [Sliding Average](gauntlex/11-data-analysis/166-moving-average/README.md) | Reviewed; authored contract retained. |
| 167 | [Scale to Unit Range](gauntlex/11-data-analysis/167-normalize-minmax/README.md) | Reviewed; authored contract retained. |
| 168 | [Multiply and Accumulate](gauntlex/11-data-analysis/168-dot-product/README.md) | Reviewed; authored contract retained. |
| 169 | [Distance in Many Dimensions](gauntlex/11-data-analysis/169-euclidean-distance/README.md) | Reviewed; authored contract retained. |
| 170 | [Add Two Grids](gauntlex/11-data-analysis/170-matrix-add/README.md) | Reviewed; authored contract retained. |
| 171 | [Matrix Composition](gauntlex/11-data-analysis/171-matrix-multiply/README.md) | Reviewed; authored contract retained. |
| 172 | [Build a Histogram](gauntlex/11-data-analysis/172-bucket-count/README.md) | Reviewed; authored contract retained. |
| 173 | [Linear Relationship](gauntlex/11-data-analysis/173-pearson-correlation/README.md) | Reviewed; authored contract retained. |
| 174 | [Running Products](gauntlex/11-data-analysis/174-cumulative-product/README.md) | Reviewed; authored contract retained. |
| 175 | [Observation Counts](gauntlex/11-data-analysis/175-frequency-table/README.md) | Reviewed; authored contract retained. |
| 176 | [Unequal Importance](gauntlex/11-data-analysis/176-weighted-mean/README.md) | Reviewed; authored contract retained. |
| 177 | [Dense Rankings](gauntlex/11-data-analysis/177-rank-values/README.md) | Reviewed; authored contract retained. |
| 178 | [Round to Steps](gauntlex/11-data-analysis/178-quantize/README.md) | Reviewed; authored contract retained. |
| 179 | [Outside the Fences](gauntlex/11-data-analysis/179-outlier-iqr/README.md) | Reviewed; authored contract retained. |
| 180 | [Fit a Straight Line](gauntlex/11-data-analysis/180-linear-regression/README.md) | Reviewed; authored contract retained. |
| 181 | [Identify the Host](gauntlex/12-http-security/181-url-host/README.md) | Reviewed; authored contract retained. |
| 182 | [Resolve a Link](gauntlex/12-http-security/182-url-join/README.md) | Reviewed; authored contract retained. |
| 183 | [Read the Response Status](gauntlex/12-http-security/183-parse-http-status/README.md) | Reviewed; authored contract retained. |
| 184 | [Canonical Header Names](gauntlex/12-http-security/184-normalize-headers/README.md) | Reviewed; authored contract retained. |
| 185 | [Read Cookie Pairs](gauntlex/12-http-security/185-parse-cookie/README.md) | Reviewed; authored contract retained. |
| 186 | [Assemble a Cookie Header](gauntlex/12-http-security/186-build-cookie/README.md) | Reviewed; authored contract retained. |
| 187 | [Backoff with a Ceiling](gauntlex/12-http-security/187-http-retry-delay/README.md) | Reviewed; authored contract retained. |
| 188 | [Page to Offset](gauntlex/12-http-security/188-pagination-offset/README.md) | Reviewed; authored contract retained. |
| 189 | [One Page of Results](gauntlex/12-http-security/189-pagination-slice/README.md) | Reviewed; authored contract retained. |
| 190 | [Match Every Field](gauntlex/12-http-security/190-query-filter/README.md) | Reviewed; authored contract retained. |
| 191 | [Build a JSON Response](gauntlex/12-http-security/191-json-response/README.md) | Reviewed; authored contract retained. |
| 192 | [Read a Bearer Token](gauntlex/12-http-security/192-parse-bearer/README.md) | Reviewed; authored contract retained. |
| 193 | [Compare Secrets Safely](gauntlex/12-http-security/193-constant-time-compare/README.md) | Reviewed; authored contract retained. |
| 194 | [Fingerprint a Message](gauntlex/12-http-security/194-sha256-hex/README.md) | Reviewed; authored contract retained. |
| 195 | [Authenticate a Message](gauntlex/12-http-security/195-hmac-signature/README.md) | Reviewed; authored contract retained. |
| 196 | [Verify a Signature](gauntlex/12-http-security/196-verify-hmac/README.md) | Reviewed; authored contract retained. |
| 197 | [Exact Origin Allowlist](gauntlex/12-http-security/197-cors-origin/README.md) | Reviewed; authored contract retained. |
| 198 | [Recognize HTTP Methods](gauntlex/12-http-security/198-http-method/README.md) | Reviewed; authored contract retained. |
| 199 | [Extract the Media Type](gauntlex/12-http-security/199-parse-content-type/README.md) | Reviewed; authored contract retained. |
| 200 | [Stable Request Identity](gauntlex/12-http-security/200-http-cache-key/README.md) | Replaced a placeholder example with stable request-key behavior. |
| 201 | [Unique Request Identifier](gauntlex/12-http-security/201-request-id/README.md) | Replaced a placeholder example with UUID format and fresh-call behavior. |
| 202 | [Escape One URL Component](gauntlex/12-http-security/202-url-encode-component/README.md) | Reviewed; authored contract retained. |
| 203 | [Restore One URL Component](gauntlex/12-http-security/203-url-decode-component/README.md) | Reviewed; authored contract retained. |
| 204 | [Decode Basic Credentials](gauntlex/12-http-security/204-parse-basic-auth/README.md) | Reviewed; authored contract retained. |
| 205 | [Find the Last Header](gauntlex/12-http-security/205-header-get/README.md) | Reviewed; authored contract retained. |
| 206 | [Define the Users Table](gauntlex/13-sqlite/206-create-users/README.md) | Reviewed; authored contract retained. |
| 207 | [Register a User](gauntlex/13-sqlite/207-insert-user/README.md) | Reviewed; authored contract retained. |
| 208 | [Find One Record](gauntlex/13-sqlite/208-find-user/README.md) | Reviewed; authored contract retained. |
| 209 | [Read the User Directory](gauntlex/13-sqlite/209-list-users/README.md) | Reviewed; authored contract retained. |
| 210 | [Change a User Email](gauntlex/13-sqlite/210-update-email/README.md) | Reviewed; authored contract retained. |
| 211 | [Remove a User](gauntlex/13-sqlite/211-delete-user/README.md) | Reviewed; authored contract retained. |
| 212 | [Search Names Literally](gauntlex/13-sqlite/212-search-users/README.md) | Reviewed; authored contract retained. Separated joined tips. |
| 213 | [Count the Directory](gauntlex/13-sqlite/213-count-users/README.md) | Reviewed; authored contract retained. |
| 214 | [Paginate User Records](gauntlex/13-sqlite/214-users-page/README.md) | Reviewed; authored contract retained. Separated joined tips. |
| 215 | [Define the Orders Table](gauntlex/13-sqlite/215-create-orders/README.md) | Reviewed; authored contract retained. Separated joined tips. |
| 216 | [Sum Customer Orders](gauntlex/13-sqlite/216-order-total/README.md) | Reviewed; authored contract retained. |
| 217 | [Rank Customers by Spending](gauntlex/13-sqlite/217-top-customers/README.md) | Reviewed; authored contract retained. |
| 218 | [Orders and Their Owners](gauntlex/13-sqlite/218-join-orders/README.md) | Reviewed; authored contract retained. |
| 219 | [Insert Only Once](gauntlex/13-sqlite/219-insert-ignore/README.md) | Reviewed; authored contract retained. |
| 220 | [Create or Replace a Score](gauntlex/13-sqlite/220-upsert-score/README.md) | Reviewed; authored contract retained. |
| 221 | [Atomic Account Transfer](gauntlex/13-sqlite/221-transaction-transfer/README.md) | Reviewed; authored contract retained. |
| 222 | [All or Nothing](gauntlex/13-sqlite/222-transaction-batch/README.md) | Reviewed; authored contract retained. |
| 223 | [Allowlisted Sorting](gauntlex/13-sqlite/223-safe-sort/README.md) | Reviewed; authored contract retained. |
| 224 | [Count Event Categories](gauntlex/13-sqlite/224-group-counts/README.md) | Reviewed; authored contract retained. |
| 225 | [Events After a Date](gauntlex/13-sqlite/225-date-filter/README.md) | Reviewed; authored contract retained. |
| 226 | [Inspect the Schema](gauntlex/13-sqlite/226-db-schema-check/README.md) | Reviewed; authored contract retained. |
| 227 | [Ensure an Index](gauntlex/13-sqlite/227-db-index/README.md) | Reviewed; authored contract retained. |
| 228 | [Store a JSON Document](gauntlex/13-sqlite/228-db-json/README.md) | Reviewed; authored contract retained. |
| 229 | [Load a JSON Document](gauntlex/13-sqlite/229-db-json-read/README.md) | Reviewed; authored contract retained. |
| 230 | [Revenue by Category](gauntlex/13-sqlite/230-db-report/README.md) | Reviewed; authored contract retained. |
| 231 | [An Awaitable Greeting](gauntlex/14-async/231-async-greeting/README.md) | Reviewed; authored contract retained. |
| 232 | [A Coroutine Result](gauntlex/14-async/232-async-double/README.md) | Reviewed; authored contract retained. |
| 233 | [Gather in Order](gauntlex/14-async/233-async-gather/README.md) | Reviewed; authored contract retained. |
| 234 | [Concurrent Transformation](gauntlex/14-async/234-async-map/README.md) | Reviewed; authored contract retained. |
| 235 | [Set a Deadline](gauntlex/14-async/235-async-timeout/README.md) | Reviewed; authored contract retained. |
| 236 | [Try Again](gauntlex/14-async/236-async-retry/README.md) | Reviewed; authored contract retained. Separated joined tips. |
| 237 | [Limit Concurrency](gauntlex/14-async/237-async-semaphore/README.md) | Documented the tested invalid-limit exception. |
| 238 | [First to Finish](gauntlex/14-async/238-async-first/README.md) | Reviewed; authored contract retained. |
| 239 | [Drain the Queue](gauntlex/14-async/239-async-queue/README.md) | Reviewed; authored contract retained. |
| 240 | [Produce in Sequence](gauntlex/14-async/240-async-producer/README.md) | Reviewed; authored contract retained. |
| 241 | [Consume Exactly N](gauntlex/14-async/241-async-consumer/README.md) | Reviewed; authored contract retained. |
| 242 | [Wait for a Signal](gauntlex/14-async/242-async-event/README.md) | Reviewed; authored contract retained. |
| 243 | [Protected Increment](gauntlex/14-async/243-async-lock/README.md) | Corrected the count key/value type description. |
| 244 | [Concurrent Selection](gauntlex/14-async/244-async-filter/README.md) | Reviewed; authored contract retained. |
| 245 | [Process in Waves](gauntlex/14-async/245-async-batch/README.md) | Documented the tested invalid-batch exception. |
| 246 | [Explain a Mismatch](gauntlex/15-testing/246-assert-equal/README.md) | Reviewed; authored contract retained. |
| 247 | [Expect a Failure](gauntlex/15-testing/247-assert-raises/README.md) | Reviewed; authored contract retained. |
| 248 | [Close Enough](gauntlex/15-testing/248-approx-equal/README.md) | Reviewed; authored contract retained. |
| 249 | [Find the Divergence](gauntlex/15-testing/249-first-difference/README.md) | Reviewed; authored contract retained. |
| 250 | [Compare Records](gauntlex/15-testing/250-diff-dicts/README.md) | Reviewed; authored contract retained. |
| 251 | [Evaluate Examples](gauntlex/15-testing/251-run-cases/README.md) | Reviewed; authored contract retained. |
| 252 | [Observe Printed Output](gauntlex/15-testing/252-capture-output/README.md) | Reviewed; authored contract retained. |
| 253 | [Check the Order](gauntlex/15-testing/253-is-sorted/README.md) | Reviewed; authored contract retained. |
| 254 | [Reject Disorder](gauntlex/15-testing/254-validate-sorted/README.md) | Reviewed; authored contract retained. |
| 255 | [Same Elements, New Order](gauntlex/15-testing/255-check-permutation/README.md) | Reviewed; authored contract retained. |
| 256 | [Guard the Nonnegative Invariant](gauntlex/15-testing/256-invariant-check/README.md) | Reviewed; authored contract retained. |
| 257 | [Count Test Report Lines](gauntlex/15-testing/257-parse-test-report/README.md) | Reviewed; authored contract retained. |
| 258 | [Measure the Failure Rate](gauntlex/15-testing/258-flaky-detector/README.md) | Reviewed; authored contract retained. |
| 259 | [Select by Name](gauntlex/15-testing/259-test-selection/README.md) | Reviewed; authored contract retained. |
| 260 | [Three Outcomes](gauntlex/15-testing/260-test-summary/README.md) | Reviewed; authored contract retained. |
| 261 | [Identify a Test](gauntlex/15-testing/261-pytest-nodeid/README.md) | Reviewed; authored contract retained. |
| 262 | [Name a Test Function](gauntlex/15-testing/262-test-name-normalize/README.md) | Reviewed; authored contract retained. |
| 263 | [Coverage Ratio](gauntlex/15-testing/263-coverage-percent/README.md) | Reviewed; authored contract retained. |
| 264 | [Spot Regressions](gauntlex/15-testing/264-regression-check/README.md) | Reviewed; authored contract retained. |
| 265 | [Cross-Platform Failures](gauntlex/15-testing/265-test-matrix/README.md) | Reviewed; authored contract retained. |
| 266 | [Undetected Mutations](gauntlex/15-testing/266-mutation-survivors/README.md) | Reviewed; authored contract retained. |
| 267 | [Unique Case Labels](gauntlex/15-testing/267-test-case-ids/README.md) | Reviewed; authored contract retained. |
| 268 | [Compare Stable Snapshots](gauntlex/15-testing/268-snapshot-compare/README.md) | Reviewed; authored contract retained. |
| 269 | [Find Slow Cases](gauntlex/15-testing/269-test-duration/README.md) | Reviewed; authored contract retained. |
| 270 | [Require Every Item](gauntlex/15-testing/270-assert-subset/README.md) | Reviewed; authored contract retained. |
| 271 | [Three-Part Version](gauntlex/16-packaging/271-semver-parse/README.md) | Reviewed; authored contract retained. |
| 272 | [Version Ordering](gauntlex/16-packaging/272-semver-compare/README.md) | Reviewed; authored contract retained. |
| 273 | [Pinned Dependency](gauntlex/16-packaging/273-dependency-parse/README.md) | Reviewed; authored contract retained. |
| 274 | [Dependency Order](gauntlex/16-packaging/274-requirements-sort/README.md) | Reviewed; authored contract retained. |
| 275 | [One Requirement per Package](gauntlex/16-packaging/275-requirements-dedupe/README.md) | Reviewed; authored contract retained. |
| 276 | [Read Environment Settings](gauntlex/16-packaging/276-env-config/README.md) | Reviewed; authored contract retained. |
| 277 | [Apply Overrides](gauntlex/16-packaging/277-config-merge/README.md) | Reviewed; authored contract retained. |
| 278 | [Describe Build Files](gauntlex/16-packaging/278-file-manifest/README.md) | Reviewed; authored contract retained. |
| 279 | [Write a Release Note](gauntlex/16-packaging/279-release-notes/README.md) | Reviewed; authored contract retained. |
| 280 | [Organize Changes](gauntlex/16-packaging/280-changelog-groups/README.md) | Reviewed; authored contract retained. |
| 281 | [Name the Entry Point](gauntlex/16-packaging/281-python-entrypoint/README.md) | Reviewed; authored contract retained. |
| 282 | [Module to File](gauntlex/16-packaging/282-module-path/README.md) | Reviewed; authored contract retained. |
| 283 | [Wheel Filename](gauntlex/16-packaging/283-artifact-name/README.md) | Reviewed; authored contract retained. |
| 284 | [Package Metadata](gauntlex/16-packaging/284-build-metadata/README.md) | Reviewed; authored contract retained. |
| 285 | [Release Readiness](gauntlex/16-packaging/285-release-checklist/README.md) | Reviewed; authored contract retained. |
| 286 | [Build in Dependency Order](gauntlex/17-architecture/286-dependency-order/README.md) | Reviewed; authored contract retained. |
| 287 | [Find Dependency Loops](gauntlex/17-architecture/287-dependency-cycles/README.md) | Reviewed; authored contract retained. |
| 288 | [Downstream Reachability](gauntlex/17-architecture/288-reachable-services/README.md) | Reviewed; authored contract retained. |
| 289 | [Who Depends on This?](gauntlex/17-architecture/289-reverse-dependencies/README.md) | Reviewed; authored contract retained. |
| 290 | [Build in Parallel Layers](gauntlex/17-architecture/290-service-layers/README.md) | Reviewed; authored contract retained. |
| 291 | [Transitive Feature Gates](gauntlex/17-architecture/291-feature-flags/README.md) | Reviewed; authored contract retained. |
| 292 | [Capture Route Parameters](gauntlex/17-architecture/292-route-match/README.md) | Reviewed; authored contract retained. |
| 293 | [Route Specificity](gauntlex/17-architecture/293-route-priority/README.md) | Reviewed; authored contract retained. |
| 294 | [Requests in a Time Window](gauntlex/17-architecture/294-rate-limit-window/README.md) | Reviewed; authored contract retained. |
| 295 | [Circuit Breaker States](gauntlex/17-architecture/295-circuit-state/README.md) | Reviewed; authored contract retained. |
| 296 | [Time to Live](gauntlex/17-architecture/296-cache-expiry/README.md) | Reviewed; authored contract retained. |
| 297 | [Evict the Oldest](gauntlex/17-architecture/297-cache-eviction/README.md) | Reviewed; authored contract retained. |
| 298 | [Worst Service Health](gauntlex/17-architecture/298-health-rollup/README.md) | Reviewed; authored contract retained. |
| 299 | [Protect the Retry Budget](gauntlex/17-architecture/299-retry-budget/README.md) | Reviewed; authored contract retained. |
| 300 | [Identify Duplicate Requests](gauntlex/17-architecture/300-idempotency-key/README.md) | Reviewed; authored contract retained. |
| 301 | [Choose a Stable Partition](gauntlex/17-architecture/301-partition-key/README.md) | Documented the tested partition-count exception. |
| 302 | [Keep First Events](gauntlex/17-architecture/302-event-dedup/README.md) | Reviewed; authored contract retained. |
| 303 | [Rebuild Account Balances](gauntlex/17-architecture/303-event-projection/README.md) | Reviewed; authored contract retained. |
| 304 | [Replay Exactly Once](gauntlex/17-architecture/304-replay-dedup/README.md) | Reviewed; authored contract retained. |
| 305 | [Configuration Changes](gauntlex/17-architecture/305-config-diff/README.md) | Reviewed; authored contract retained. |
| 306 | [Permission by Role](gauntlex/17-architecture/306-permission-check/README.md) | Reviewed; authored contract retained. |
| 307 | [Inherited Permissions](gauntlex/17-architecture/307-permission-inherit/README.md) | Reviewed; authored contract retained. |
| 308 | [Record an Action](gauntlex/17-architecture/308-audit-record/README.md) | Reviewed; authored contract retained. |
| 309 | [Structured Errors](gauntlex/17-architecture/309-error-envelope/README.md) | Distinguished explicit None from an omitted required argument. |
| 310 | [Opaque Page Cursor](gauntlex/17-architecture/310-pagination-token/README.md) | Reviewed; authored contract retained. |
| 311 | [Persistent Task Tracker](gauntlex/18-capstones/311-task-tracker/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 312 | [Streaming Log Inspector](gauntlex/18-capstones/312-log-analyzer/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 313 | [Expense Ledger](gauntlex/18-capstones/313-expense-ledger/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 314 | [A Minimal HTTP Service](gauntlex/18-capstones/314-http-api-server/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 315 | [Safe Relative Paths](gauntlex/19-file-automation/315-safe-relative-path/README.md) | Reviewed; authored contract retained. |
| 316 | [Recognize File Extensions](gauntlex/19-file-automation/316-file-extension/README.md) | Reviewed; authored contract retained. |
| 317 | [One Line Ending](gauntlex/19-file-automation/317-line-ending-normalize/README.md) | Reviewed; authored contract retained. |
| 318 | [Read an INI Section](gauntlex/19-file-automation/318-parse-ini-section/README.md) | Reviewed; authored contract retained. |
| 319 | [Follow Nested Keys](gauntlex/19-file-automation/319-json-path-get/README.md) | Reviewed; authored contract retained. |
| 320 | [Flatten a JSON Tree](gauntlex/19-file-automation/320-flatten-json/README.md) | Reviewed; authored contract retained. |
| 321 | [Rebuild Nested JSON](gauntlex/19-file-automation/321-unflatten-json/README.md) | Reviewed; authored contract retained. |
| 322 | [Fingerprint a File](gauntlex/19-file-automation/322-file-checksum/README.md) | Reviewed; authored contract retained. |
| 323 | [Count File Records](gauntlex/19-file-automation/323-count-file-lines/README.md) | Reviewed; authored contract retained. |
| 324 | [Append Structured Records](gauntlex/19-file-automation/324-append-jsonl/README.md) | Reviewed; authored contract retained. |
| 325 | [Load a JSON Lines Stream](gauntlex/19-file-automation/325-read-jsonl/README.md) | Reviewed; authored contract retained. |
| 326 | [Replace a File Safely](gauntlex/19-file-automation/326-write-atomic/README.md) | Reviewed; authored contract retained. |
| 327 | [Find Duplicate Content](gauntlex/19-file-automation/327-find-duplicates/README.md) | Reviewed; authored contract retained. |
| 328 | [Aggregate CSV Values](gauntlex/19-file-automation/328-csv-group-sum/README.md) | Reviewed; authored contract retained. |
| 329 | [Count Unique CSV Rows](gauntlex/19-file-automation/329-csv-dedupe/README.md) | Reviewed; authored contract retained. |
| 330 | [Map a Directory](gauntlex/19-file-automation/330-directory-manifest/README.md) | Reviewed; authored contract retained. |
| 331 | [Select File Types](gauntlex/19-file-automation/331-filter-by-suffix/README.md) | Reviewed; authored contract retained. |
| 332 | [Inspect Archive Paths](gauntlex/19-file-automation/332-safe-archive-name/README.md) | Reviewed; authored contract retained. |
| 333 | [Plan Log Backups](gauntlex/19-file-automation/333-rotate-logs/README.md) | Documented the tested backup-count exception. |
| 334 | [Fingerprint Configuration](gauntlex/19-file-automation/334-config-fingerprint/README.md) | Reviewed; authored contract retained. |
| 335 | [Your First WSGI Response](gauntlex/20-wsgi-web/335-wsgi-health/README.md) | Reviewed; authored contract retained. |
| 336 | [Route by Path](gauntlex/20-wsgi-web/336-wsgi-routing/README.md) | Reviewed; authored contract retained. |
| 337 | [Method Matters](gauntlex/20-wsgi-web/337-wsgi-method/README.md) | Reviewed; authored contract retained. |
| 338 | [Decode Query Input](gauntlex/20-wsgi-web/338-wsgi-query/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 339 | [Serialize a Web Response](gauntlex/20-wsgi-web/339-wsgi-json/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 340 | [Read a Request Body](gauntlex/20-wsgi-web/340-wsgi-post-body/README.md) | Reviewed; authored contract retained. |
| 341 | [Validate JSON Input](gauntlex/20-wsgi-web/341-wsgi-json-post/README.md) | Reviewed; authored contract retained. |
| 342 | [Inspect Request Headers](gauntlex/20-wsgi-web/342-wsgi-headers/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 343 | [Headers Without a Body](gauntlex/20-wsgi-web/343-wsgi-head/README.md) | Reviewed; authored contract retained. |
| 344 | [Move a Resource](gauntlex/20-wsgi-web/344-wsgi-redirect/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 345 | [Recognize a Session Cookie](gauntlex/20-wsgi-web/345-wsgi-cookie/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 346 | [Protect a Private Route](gauntlex/20-wsgi-web/346-wsgi-auth/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 347 | [Control Cross-Origin Access](gauntlex/20-wsgi-web/347-wsgi-cors/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 348 | [Avoid Unchanged Responses](gauntlex/20-wsgi-web/348-wsgi-conditional/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 349 | [Safe Server Errors](gauntlex/20-wsgi-web/349-wsgi-error-handler/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 350 | [Validate Request IDs](gauntlex/20-wsgi-web/350-wsgi-request-id/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 351 | [Count Response Bytes](gauntlex/20-wsgi-web/351-wsgi-content-length/README.md) | Documented the missing-method GET assumption used by existing callable checks. |
| 352 | [Read Form Fields](gauntlex/20-wsgi-web/352-wsgi-form/README.md) | Reviewed; authored contract retained. |
| 353 | [Consistent Not Found](gauntlex/20-wsgi-web/353-wsgi-not-found-json/README.md) | Reviewed; authored contract retained. |
| 354 | [Wrap an Application](gauntlex/20-wsgi-web/354-wsgi-middleware/README.md) | Reviewed; authored contract retained. |
| 355 | [Scale to Zero and One](gauntlex/21-data-science/355-min-max-scale/README.md) | Reviewed; authored contract retained. |
| 356 | [Standardize Observations](gauntlex/21-data-science/356-z-score-scale/README.md) | Reviewed; authored contract retained. |
| 357 | [Smooth with Windows](gauntlex/21-data-science/357-moving-average/README.md) | Reviewed; authored contract retained. |
| 358 | [Weighted Recent History](gauntlex/21-data-science/358-exponential-smoothing/README.md) | Named the tested alpha exception. |
| 359 | [Weighted Observations](gauntlex/21-data-science/359-weighted-mean/README.md) | Named the tested length-mismatch exception. |
| 360 | [Move Together](gauntlex/21-data-science/360-covariance/README.md) | Reviewed; authored contract retained. |
| 361 | [Interpolate a Quantile](gauntlex/21-data-science/361-quantile-linear/README.md) | Reviewed; authored contract retained. |
| 362 | [Classify the Outcomes](gauntlex/21-data-science/362-confusion-matrix/README.md) | Reviewed; authored contract retained. |
| 363 | [Measure a Classifier](gauntlex/21-data-science/363-classification-metrics/README.md) | Reviewed; authored contract retained. |
| 364 | [Average Prediction Error](gauntlex/21-data-science/364-mean-absolute-error/README.md) | Reviewed; authored contract retained. |
| 365 | [Penalize Large Errors](gauntlex/21-data-science/365-root-mean-square-error/README.md) | Reviewed; authored contract retained. |
| 366 | [Explain the Variation](gauntlex/21-data-science/366-r-squared/README.md) | Documented the tested empty/mismatched-input exception. |
| 367 | [Straight-Line Distance](gauntlex/21-data-science/367-euclidean-distance/README.md) | Reviewed; authored contract retained. |
| 368 | [Compare Directions](gauntlex/21-data-science/368-cosine-similarity/README.md) | Reviewed; authored contract retained. |
| 369 | [City-Block Distance](gauntlex/21-data-science/369-manhattan-distance/README.md) | Reviewed; authored contract retained. |
| 370 | [Find Nearby Examples](gauntlex/21-data-science/370-k-nearest-neighbors/README.md) | Reviewed; authored contract retained. |
| 371 | [Hold Out Examples](gauntlex/21-data-science/371-train-test-split/README.md) | Reviewed; authored contract retained. |
| 372 | [Train in Batches](gauntlex/21-data-science/372-minibatches/README.md) | Reviewed; authored contract retained. |
| 373 | [Encode Categories](gauntlex/21-data-science/373-one-hot-encode/README.md) | Reviewed; authored contract retained. |
| 374 | [Normalize Each Feature](gauntlex/21-data-science/374-standardize-columns/README.md) | Reviewed; authored contract retained. |
| 375 | [First Not Smaller](gauntlex/22-advanced-algorithms/375-binary-search-bound/README.md) | Reviewed; authored contract retained. |
| 376 | [First Strictly Greater](gauntlex/22-advanced-algorithms/376-upper-bound/README.md) | Reviewed; authored contract retained. |
| 377 | [Merge Integer Ranges](gauntlex/22-advanced-algorithms/377-merge-intervals/README.md) | Reviewed; authored contract retained. |
| 378 | [Where Ranges Overlap](gauntlex/22-advanced-algorithms/378-interval-intersection/README.md) | Reviewed; authored contract retained. |
| 379 | [Longest Distinct Window](gauntlex/22-advanced-algorithms/379-longest-unique-substring/README.md) | Reviewed; authored contract retained. |
| 380 | [Smallest Covering Substring](gauntlex/22-advanced-algorithms/380-minimum-window/README.md) | Reviewed; authored contract retained. |
| 381 | [Frequency with Stable Ties](gauntlex/22-advanced-algorithms/381-top-k-frequent/README.md) | Reviewed; authored contract retained. |
| 382 | [Shortest Grid Route](gauntlex/22-advanced-algorithms/382-shortest-path-grid/README.md) | Reviewed; authored contract retained. |
| 383 | [Weighted Shortest Paths](gauntlex/22-advanced-algorithms/383-dijkstra-distances/README.md) | Removed a contradictory unreachable-node sentinel. |
| 384 | [Increasing Subsequence](gauntlex/22-advanced-algorithms/384-longest-increasing-subsequence/README.md) | Reviewed; authored contract retained. |
| 385 | [Shift the Alphabet](gauntlex/23-security-crypto/385-caesar-cipher/README.md) | Reviewed; authored contract retained. |
| 386 | [Half an Alphabet](gauntlex/23-security-crypto/386-rot13/README.md) | Reviewed; authored contract retained. |
| 387 | [Text to Hexadecimal](gauntlex/23-security-crypto/387-hex-encode/README.md) | Reviewed; authored contract retained. |
| 388 | [Hexadecimal to Text](gauntlex/23-security-crypto/388-hex-decode/README.md) | Reviewed; authored contract retained. |
| 389 | [Encode Base64](gauntlex/23-security-crypto/389-base64-encode/README.md) | Reviewed; authored contract retained. |
| 390 | [Decode Base64](gauntlex/23-security-crypto/390-base64-decode/README.md) | Reviewed; authored contract retained. |
| 391 | [Sign a Message](gauntlex/23-security-crypto/391-hmac-sign/README.md) | Reviewed; authored contract retained. |
| 392 | [Authenticate a Signature](gauntlex/23-security-crypto/392-hmac-verify/README.md) | Reviewed; authored contract retained. |
| 393 | [Derive a Key](gauntlex/23-security-crypto/393-pbkdf2-key/README.md) | Reviewed; authored contract retained. |
| 394 | [Secure Random Token](gauntlex/23-security-crypto/394-random-token/README.md) | Named the tested token-size exception. |
| 395 | [Rule-Based Password Score](gauntlex/23-security-crypto/395-password-strength/README.md) | Reviewed; authored contract retained. |
| 396 | [Reveal Only the End](gauntlex/23-security-crypto/396-mask-secret/README.md) | Named the tested visible-count exception. |
| 397 | [Canonical IPv4](gauntlex/23-security-crypto/397-validate-ipv4/README.md) | Corrected the leading-zero explanation. |
| 398 | [Normalize a Network](gauntlex/23-security-crypto/398-cidr-network/README.md) | Reviewed; authored contract retained. |
| 399 | [Network Membership](gauntlex/23-security-crypto/399-cidr-contains/README.md) | Reviewed; authored contract retained. |
| 400 | [Inspect a Web Host](gauntlex/23-security-crypto/400-safe-url-host/README.md) | Reviewed; authored contract retained. |
| 401 | [Hide Sensitive Headers](gauntlex/23-security-crypto/401-redact-headers/README.md) | Reviewed; authored contract retained. |
| 402 | [Allowlisted Query Parameters](gauntlex/23-security-crypto/402-query-param-filter/README.md) | Reviewed; authored contract retained. |
| 403 | [Summarize Security Events](gauntlex/23-security-crypto/403-security-event-counts/README.md) | Reviewed; authored contract retained. |
| 404 | [Timing-Resistant Equality](gauntlex/23-security-crypto/404-constant-time-match/README.md) | Reviewed; authored contract retained. |
| 405 | [Inventory Manager](gauntlex/18-capstones/405-inventory-manager/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 406 | [Contact Directory](gauntlex/18-capstones/406-contact-book/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 407 | [CSV Data Pipeline](gauntlex/18-capstones/407-csv-etl-pipeline/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 408 | [Event-Sourced Wallet](gauntlex/18-capstones/408-event-sourced-wallet/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
| 409 | [Local Link Inspector](gauntlex/18-capstones/409-markdown-link-checker/README.md) | Restructured the existing project contract into verifiable command, data, output, and failure requirements. |
