# Persistent Task Tracker

## Description
Build a task-management command-line application whose data survives between runs. Users must be able to add, list, complete, and remove tasks.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Commands: `python main.py add TITLE`, `list`, `done ID`, and `delete ID`. Store tasks in a SQLite file specified by `TASK_DB` environment variable; default `tasks.db` in the working directory. The list command prints compact sorted-key JSON of all tasks ordered by ID, with objects `{id:int,title:str,done:bool}`. Add prints the new integer ID, done/delete print `ok` on success and `not found` otherwise. Unknown commands return exit status 2 and print usage to stderr. Titles must not be empty after trimming.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Design the CLI so every command operates on the same persisted SQLite state across separate invocations. Treat malformed titles and missing task IDs as distinct cases.

## Example Behavior
Adding a task and then listing tasks in a fresh process must still show the new task; an unknown command exits with status 2.

## Tips
Separate command parsing from persistence. Think through missing IDs, empty titles, and stable record ordering.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
