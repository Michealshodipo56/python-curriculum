# Task Tracker CLI

## Project brief
Build a persistent command-line task tracker using SQLite.

## Acceptance contract
Commands: `python main.py add TITLE`, `list`, `done ID`, and `delete ID`. Store tasks in a SQLite file specified by `TASK_DB` environment variable; default `tasks.db` in the working directory. The list command prints compact sorted-key JSON of all tasks ordered by ID, with objects `{id:int,title:str,done:bool}`. Add prints the new integer ID, done/delete print `ok` on success and `not found` otherwise. Unknown commands return exit status 2 and print usage to stderr. Titles must not be empty after trimming.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the complete working project in `starter/main.py` and any additional modules under `starter/`.
- Add your own unit and integration tests beyond the provided acceptance checks.
- Document architecture, failure modes, and how to run the program.

## AI Guide policy
The Guide may ask about architecture, input contracts, and debugging, but must never provide full code or a working answer.

## AI Auditor defense
Explain your architecture, show a passing end-to-end test, and justify how you handle invalid inputs and persistence or service lifecycle.
