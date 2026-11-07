# Persistent Task Tracker

## Description

Build a task-management command-line application whose data survives between runs. Users must be able to add, list, complete, and remove tasks.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run commands from `starter/` as `python main.py add TITLE`, `python main.py list`, `python main.py done ID`, or `python main.py delete ID`.
- Persist tasks in SQLite at the `TASK_DB` environment-variable path, defaulting to `tasks.db` in the working directory.
- Reject a title that is empty after trimming surrounding whitespace.
- `add` prints the new integer ID. Each task has an integer `id`, string `title`, and Boolean `done` value, initially `false`.
- `list` prints a compact JSON array of all tasks in ascending ID order, with object keys sorted. An empty database produces `[]`.
- `done` and `delete` print `ok` for an existing ID or `not found` otherwise. Completing a task sets its `done` value to `true`.
- Unknown commands exit with status `2` and print usage to standard error.
- Preserve data across separate process runs and end each printed result with a newline.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain the task schema, ID handling, and persistence across commands.

## Design Considerations

Design the CLI so every command operates on the same persisted SQLite state across separate invocations. Treat malformed titles and missing task IDs as distinct cases.

## Example Behavior

Adding a task and then listing tasks in a fresh process must still show the new task; an unknown command exits with status 2.

## Tips

Separate command parsing from persistence. Think through missing IDs, empty titles, and stable record ordering.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
