# Curriculum review work log

## Scope and source baseline

- User requested a content-reviewed, prerequisite-ordered unification, not the preliminary inventory's order.
- The canonical local checkout is `gauntlex/python-curriculum`; its remote was renamed from `gauntlex-python` to `python-curriculum`.
- Started from local parent commit `49eba29333e95228d5fae21ca9d9d909e2fd4f77`; fast-forwarded to remote `1be1255c300130ea234dcc3174282ab39ccc2482` to include the preliminary Markdown inventory.
- The four source trees are Git submodules, not copied files. Their commits are pinned below and were verified on GitHub. Added missing `.gitmodules` mappings without changing any gitlink commit or source file.
- No changes are intended inside the four source repositories. `learn.python/AGENTS.md` was read; the user's explicit re-sequencing request takes precedence over its tutor-session sequencing rules. No subagents were requested or used.

| Source | Pinned commit | Source URL |
| --- | --- | --- |
| Exercism (`python-curriculum`) | `6105f6d9d3ef66ce3d5c8f529d2882af3d76b706` | https://github.com/exercism/python |
| `30-Days-Of-Python` | `50c11a80a6e3924a7be58c89f409697e12cb4d70` | https://github.com/Michealshodipo56/30-Days-Of-Python |
| `C1-Code-Crunch-Convos` | `ccd5dc1dc015b3c485a2a69906145a5d492b0585` | https://github.com/Michealshodipo56/C1-Code-Crunch-Convos |
| `learn.python` | `c119a512789e3c76b2456c390a910960c8debd3a` | https://github.com/Michealshodipo56/learn.python |

## Review status

Work is in progress. Nothing in this log is a completion claim.

- Initial exhaustive byte scan: 5,655 source files, excluding Git internals. Records include content hashes, syntax analysis, document headings, links, and import/assertion information where applicable.
- Automated scanning is distinct from semantic task review. Review packets show actual task instructions and code/test contracts; decisions must be recorded against those packets before generation.
- Initial parser flagged a UTF-16 Russian README and CSV as binary; encoding handling was corrected and inventory must be regenerated before final coverage reporting.
- Dataset rows and image/vendor assets are supporting resources, not separate assignments. Resource validation and exclusion accounting remain required.
- Preliminary discovery: 163 Exercism units (21 concept, 142 practice); 253 `learn.python` projects including 15 absolute-beginner exercises; 60 non-solution challenge scripts; 179 C1 assignment pages; other guides, quizzes, project variants, and individual 30 Days questions require detailed review.
- Meaningful tasks must be classified as core, practice, challenge, or project. Exact duplicates and alternate representations require explicit reasons and mappings, not silent deletion.

## Content findings to carry into sequencing

- C1's initial Hello World task uses `sys`, functions, annotations, the main guard, f-strings, a virtual environment, and Git. It cannot be the absolute beginner's first independent assignment without earlier instruction in those skills.
- `learn.python` Terminal Hello Lab is an implemented program with required Alter/Break/Fix/Explain work, not a blank starter. It also uses functions, annotations, dictionaries, loops, string methods, input conversion, and pytest. Place its complete required work after those prerequisites.
- C1 assignment pages contain inline worked solutions. Assign the brief/requirements, never the solution sections or complete companion answer scripts.
- Exercism's `files.solution` means learner-facing starter, whereas `.meta/example.py` and `.meta/exemplar.py` are reference answers. Do not confuse the two.
- The preliminary curriculum duplicates entire project lists across stages and includes container directories as projects. It is not authoritative and must be replaced.

## Tooling and pending checks

- Runtime: bundled CPython 3.12.14. A repository-local ignored `.venv` contains pytest 9.1.1. Pillow, pandas, numpy, and pypdf are available in the bundled interpreter.
- Original Exercism reference implementations pass all 163 supplied suites (2,377 test methods). These checks do not establish that prose and tests agree; semantic defects remain separately recorded.
- Semantic task decisions are accumulating in `review/task_notes.tsv`: all 21 Exercism concept units, all 142 practice units, and 15 learn.python level-00 activities have been reviewed through content-bearing views. Packet logs record views, not a guarantee that every source line was manually reviewed. Remaining source work is still pending.
- Separate refactoring-baseline check: Markdown and Ledger supplied baselines pass their local tests; Tree Building has six failures caused by legacy vague exception messages (35 passing, six failing across these three suites). This is distinct from the all-passing instructor references. Assign Tree Building with an explicit baseline/error-contract warning.
- Additional exclusions identified through contents: Octal contradicts its invalid-input tests; Point Mutations is an explicitly replaced Hamming variant with contradictory unequal-length cases. Minesweeper is a near-identical Flower Field predecessor and should become an alternate link on that assignment rather than another numbered task.
- `tools/curriculum_inventory.py`: full byte/text/AST inventory, Git internals pruned.
- `tools/discover_curriculum.py`: candidate discovery only; no sequencing decisions.
- `tools/review_packets.py`: content-bearing brief and AST-contract views; logs views, not a claim of complete manual line-by-line review.
- Pending: full semantic review, duplicate and defect decisions, task-level prerequisite graph, final Markdown generation, per-source coverage/exclusion report, validation, commit and push.

## 30 Days question-review checkpoint

- Full numbered exercise blocks reviewed:286 parent questions across29 files (days1-26,28-29 and root numpy.md). Nested subrequirements stay with parent questions. Days27 and30 have no numbered questions; both full chapters were read, and Day27 contains guided database work that still needs its own retained learning unit.
- Per-question decisions are reproducibly materialized by `tools/record_30days_review.py` into `review/30days_decisions.json`. Shared skill defaults are provisional and need finer final prerequisite sequencing; they are not a completed learning graph.
- Several full teaching chapters were read as recorded in `SOURCE_QUALITY_NOTES.md`; early lesson gaps and generated output-table limits remain explicitly listed. Numbered prompts being reviewed does not mean the entire source repository has completed semantic review.
- Read-only external-resource results are in `review/external_resource_checks.json`. UCI original listing redirects to404; Wikipedia table returned200. Cat API returned403 in this environment; other failures include certificate verification and disconnected demos. No insecure certificate bypass or silent URL replacement was used.
- Inventory rerun reads5655 source files:5565 text and90 binary. Russian README is UTF16; remaining binary resources still need resource-specific validation.
