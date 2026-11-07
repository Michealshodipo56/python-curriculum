# Create or Replace a Score

## Description

Maintain exactly one score per student, creating a record on first use and updating it on later submissions.

## Requirements

- Implement `upsert_score(conn, student, score)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `scores(student TEXT PRIMARY KEY,score INTEGER)` exists.
- Insert a new student and score when the student is absent.
- Overwrite the score when that student already exists.
- Do not create duplicate student rows.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips

- What determines whether the operation is an insert or an update?
- Why is the student key central to the behavior?

## Example Behavior

Calling `upsert_score` twice for one student leaves one row with the newer score.
