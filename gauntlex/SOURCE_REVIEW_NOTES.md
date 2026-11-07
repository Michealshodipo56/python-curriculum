# Pinned source review — first four samples

These are **manual content comparisons**, not automated title matching. The four source roots are git submodules; the files below were read at the exact pinned commits.

| Source | Pinned revision | Source file | Finding | Coverage decision |
|---|---|---|---|---|
| learn.python | `c119a512789e3c76b2456c390a910960c8debd3a` | `projects/level-00-absolute-beginner/02-hello-world/exercise.py` | A tutorial-style script demonstrates several print operations: text, numbers, arithmetic, multiple arguments and blank lines. | **Unmapped.** Gauntlex 001 covers only a single print statement; it does not replace the complete source exercise. |
| C1-Code-Crunch-Convos | `ccd5dc1dc015b3c485a2a69906145a5d492b0585` | `curriculum/week-01-python-foundations/homework/problem-01-verify-your-install.md` | Learner must verify a local Python installation and produce terminal evidence. | **Unmapped.** A code-grading exercise cannot establish the learner's local installation; this needs a manual/evidence-based task. |
| 30-Days-Of-Python | `50c11a80a6e3924a7be58c89f409697e12cb4d70` | `02_Day_Variables_builtin_functions/02_variables_builtin_functions.md` | A lesson and exercise collection on built-in functions, variables and data types. | **Unmapped.** Requires splitting lesson outcomes into individual Gauntlex tasks and checking each outcome. |
| Exercism Python | `6105f6d9d3ef66ce3d5c8f529d2882af3d76b706` | `exercises/practice/hello-world/.docs/instructions.md` | Requires the exact output string `Hello, World!` (capital W). | **Unmapped.** Gauntlex 001 requires `Hello, world!` (lowercase w), so these are not identical acceptance contracts. |

## Why this matters

The curriculum index lists source materials of **different granularity**: tutorials, day-long lessons, evidence-based assignments, and individual programming exercises. One Gauntlex task is not necessarily equivalent to one source index entry. Source coverage must compare the actual learning outcomes and acceptance contracts, not merely names.

## Next review procedure

For each assigned source entry: read its pinned content, identify assessable outcomes, compare Gauntlex briefs and tests, record exact mapping(s) only after equivalence is verified, and separately record outcomes requiring a new task or manual evaluation. Do not modify source licenses or publish source solutions in learner packages.
