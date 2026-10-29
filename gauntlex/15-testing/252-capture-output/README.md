# capture_output

## Challenge
Call zero-argument fn and return [result,stdout_text] with everything printed to stdout during the call. Restore stdout even if fn raises, and propagate its exception.

## Requirements
- Implement `capture_output(fn)` in `starter/solution.py`.
- Return the specified value or raise the specified exception.
- Do not mutate input data, print, or require external packages.
- Use the Python standard library only.

## Hints
redirect_stdout and StringIO can capture prints safely.

## Run tests
`python -m pytest tests -q`
