# Student Averages

## Description

A gradebook records multiple scores for each student and reports their average. Distinguish students with no recorded scores from those with a genuine average of zero.

## Requirements

- Define `Gradebook` in `starter/solution.py`.
- Implement `add_score(student, score)` to record a score for a student.
- Accept scores only from `0` through `100`, inclusive; raise `ValueError` for an out-of-range score.
- Implement `average(student)` to return the arithmetic mean of recorded scores.
- Return `None` when the student has no scores.
- Use Python's standard library only and do not print or request input at import time.

## Tips

- Why does a missing average differ from an average of zero?
- How should repeated scores for one student affect the result?

## Example Behavior

After adding scores `80` and `100` for `'Ada'`, `average('Ada')` returns `90`; an unknown student returns `None`.
